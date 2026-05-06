from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count, Avg
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import Student, ExamSession, ViolationScreenshot

def index(request):
    """Login page with regno and password"""
    return render(request, 'login.html')

def register_page(request):
    """Registration page for new students"""
    return render(request, 'register.html')

def exam_page(request):
    """Exam monitoring page - Only accessible by logged-in student"""
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('index')
    
    try:
        student = Student.objects.get(id=student_id)
        # Only return the logged-in student's data
        return render(request, 'exam.html', {'student': student})
    except:
        request.session.flush()
        return redirect('index')

@csrf_exempt
def student_login(request):
    """Handle student login with regno and password"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            regno = data.get('regno')
            password = data.get('password')
            
            try:
                student = Student.objects.get(register_no=regno)
                if student.check_password(password):
                    # Create exam session
                    session = ExamSession.objects.create(student=student)
                    
                    request.session['student_id'] = student.id
                    request.session['session_id'] = session.id
                    
                    return JsonResponse({
                        'success': True,
                        'student': {
                            'name': student.name,
                            'regno': student.register_no
                        },
                        'session_id': session.id
                    })
                else:
                    return JsonResponse({'success': False, 'error': 'Invalid password'}, status=401)
            except Student.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Register number not found'}, status=404)
                
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@csrf_exempt
def student_signup(request):
    """Handle student signup"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Check if student already exists
            if Student.objects.filter(register_no=data['regno']).exists():
                return JsonResponse({'success': False, 'error': 'Register number already exists'}, status=400)
            
            # Create new student
            student = Student(
                name=data['name'],
                phone=data['phone'],
                email=data.get('email', ''),
                college_name=data['college'],
                register_no=data['regno']
            )
            student.set_password(data['password'])
            student.save()
            
            # Send email notification to admin
            try:
                admin_subject = f'🎓 New Student Registration - {student.name}'
                admin_message = f'''New Student Registered on ExamGuard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 STUDENT DETAILS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 Full Name:           {student.name}
🪪 Register Number:     {student.register_no}
📧 Email Address:       {student.email}
📱 Phone Number:        {student.phone}
🏫 College/University:  {student.college_name}
📅 Registration Date:   {timezone.now().strftime("%B %d, %Y")}
⏰ Registration Time:   {timezone.now().strftime("%I:%M %p")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 ACCOUNT STATUS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Account Created Successfully
✅ Password Encrypted and Stored Securely
✅ Ready to Take Exams

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 ADMIN ACTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

View Student Details: http://localhost:8000/admin-api/students/
Manage All Students:  http://localhost:8000/admin/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is an automated notification from ExamGuard.

🛡️ ExamGuard - Secure Online Exams with AI
'''
                
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['examprivate86@gmail.com'],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Admin email error: {e}")
            
            # Send welcome email to student
            if student.email:
                try:
                    student_subject = '🎓 Welcome to ExamGuard - Account Created Successfully'
                    student_message = f'''Dear {student.name},

Welcome to ExamGuard! Your account has been created successfully.

📋 Your Account Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Full Name: {student.name}
🪪 Register Number: {student.register_no}
📱 Phone: {student.phone}
📧 Email: {student.email}
🏫 College: {student.college_name}
📅 Account Created: {timezone.now().strftime("%B %d, %Y at %I:%M %p")}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 Security Information:
• Your password is securely encrypted
• Keep your credentials confidential
• Do not share your login details

📷 Exam Monitoring Rules:
• Only one person allowed in frame
• Face must remain visible at all times
• No looking away for more than 2 seconds
• Sleep/drowsiness will be detected
• Head must stay within camera view

⚠️ Important:
Any violation of the above rules will immediately terminate your exam session.

🚀 Ready to Start?
Login at: http://localhost:8000

Thank you for choosing ExamGuard!

Best regards,
ExamGuard Team
🛡️ Secure Online Exams with AI
'''
                    send_mail(
                        student_subject,
                        student_message,
                        settings.DEFAULT_FROM_EMAIL,
                        [student.email],
                        fail_silently=True,
                    )
                except Exception as e:
                    print(f"Student email error: {e}")
            
            # Create exam session
            session = ExamSession.objects.create(student=student)
            
            request.session['student_id'] = student.id
            request.session['session_id'] = session.id
            
            return JsonResponse({
                'success': True,
                'student': {
                    'name': student.name,
                    'regno': student.register_no
                },
                'session_id': session.id
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@csrf_exempt
def log_violation(request):
    """Log violation - Only for logged-in student's own session"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = request.session.get('session_id')
            student_id = request.session.get('student_id')
            
            # Security check: Ensure student is logged in
            if not session_id or not student_id:
                return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=401)
            
            # Security check: Verify session belongs to logged-in student
            session = ExamSession.objects.get(id=session_id, student_id=student_id)
            
            session.violations += 1
            reasons = session.violation_reasons
            if reasons:
                reasons += f", {data['reason']}"
            else:
                reasons = data['reason']
            session.violation_reasons = reasons
            session.status = 'terminated'
            session.ended_at = timezone.now()
            session.save()
            
            return JsonResponse({'success': True, 'violations': session.violations})
        except ExamSession.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Unauthorized access'}, status=403)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False}, status=400)

@csrf_exempt
def logout_view(request):
    """Logout and end session - Only for logged-in student's own session"""
    if request.method == 'POST':
        session_id = request.session.get('session_id')
        student_id = request.session.get('student_id')
        
        if session_id and student_id:
            try:
                # Security check: Verify session belongs to logged-in student
                session = ExamSession.objects.get(id=session_id, student_id=student_id)
                session.ended_at = timezone.now()
                if session.status == 'active':
                    session.status = 'completed'
                session.save()
            except ExamSession.DoesNotExist:
                pass
        
        request.session.flush()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@staff_member_required
def students_management(request):
    """Students management page"""
    students = Student.objects.all().order_by('-id')
    students_json = json.dumps([{
        'id': s.id,
        'name': s.name,
        'register_no': s.register_no,
        'email': s.email,
        'phone': s.phone,
        'college_name': s.college_name,
        'sessions_count': s.examsession_set.count()
    } for s in students])
    
    return render(request, 'admin/students.html', {
        'students': students,
        'students_json': students_json
    })

@staff_member_required
@csrf_exempt
def create_student(request):
    """Create new student"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if Student.objects.filter(register_no=data['register_no']).exists():
                return JsonResponse({'success': False, 'error': 'Register number already exists'}, status=400)
            
            student = Student(
                name=data['name'],
                register_no=data['register_no'],
                email=data['email'],
                phone=data['phone'],
                college_name=data['college_name']
            )
            if data.get('password'):
                student.set_password(data['password'])
            student.save()
            
            return JsonResponse({'success': True, 'student_id': student.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@staff_member_required
@csrf_exempt
def update_student(request, student_id):
    """Update student"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=student_id)
            
            # Check if register number is taken by another student
            if Student.objects.filter(register_no=data['register_no']).exclude(id=student_id).exists():
                return JsonResponse({'success': False, 'error': 'Register number already exists'}, status=400)
            
            student.name = data['name']
            student.register_no = data['register_no']
            student.email = data['email']
            student.phone = data['phone']
            student.college_name = data['college_name']
            
            if data.get('password'):
                student.set_password(data['password'])
            
            student.save()
            
            return JsonResponse({'success': True})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@staff_member_required
@csrf_exempt
def delete_student(request, student_id):
    """Delete student"""
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({'success': True})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@staff_member_required
def violations_report(request):
    """Violations report page"""
    sessions = ExamSession.objects.filter(violations__gt=0).select_related('student').order_by('-violations', '-started_at')
    
    # Calculate statistics
    total_violations = sessions.aggregate(Sum('violations'))['violations__sum'] or 0
    total_students_with_violations = sessions.values('student').distinct().count()
    terminated_sessions = sessions.filter(status='terminated').count()
    avg_violations = round(sessions.aggregate(Avg('violations'))['violations__avg'] or 0, 1)
    
    # Prepare sessions data for JSON
    sessions_json = json.dumps([{
        'id': s.id,
        'student_name': s.student.name,
        'student_regno': s.student.register_no,
        'student_email': s.student.email,
        'student_college': s.student.college_name,
        'status': s.status,
        'violations': s.violations,
        'violation_reasons': s.violation_reasons or '',
        'started_at': s.started_at.strftime('%B %d, %Y %H:%M'),
        'ended_at': s.ended_at.strftime('%B %d, %Y %H:%M') if s.ended_at else None,
        'duration': str(s.ended_at - s.started_at).split('.')[0] if s.ended_at else 'In Progress'
    } for s in sessions])
    
    # Add duration property to sessions for template
    for session in sessions:
        if session.ended_at:
            duration = session.ended_at - session.started_at
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            seconds = duration.seconds % 60
            session.duration = f"{hours}h {minutes}m {seconds}s" if hours > 0 else f"{minutes}m {seconds}s"
        else:
            session.duration = 'In Progress'
    
    return render(request, 'admin/violations.html', {
        'sessions': sessions,
        'sessions_json': sessions_json,
        'total_violations': total_violations,
        'total_students_with_violations': total_students_with_violations,
        'terminated_sessions': terminated_sessions,
        'avg_violations': avg_violations
    })

@staff_member_required
@csrf_exempt
def clear_violations(request, session_id):
    """Clear violations for a session"""
    if request.method == 'POST':
        try:
            session = ExamSession.objects.get(id=session_id)
            session.violations = 0
            session.violation_reasons = ''
            session.save()
            return JsonResponse({'success': True})
        except ExamSession.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Session not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@staff_member_required
def sessions_management(request):
    """Sessions management page"""
    sessions = ExamSession.objects.all().select_related('student').order_by('-started_at')
    all_students = Student.objects.all().order_by('name')
    
    # Calculate statistics
    total_sessions = sessions.count()
    active_sessions = sessions.filter(status='active').count()
    completed_sessions = sessions.filter(status='completed').count()
    terminated_sessions = sessions.filter(status='terminated').count()
    
    # Prepare sessions data for JSON
    sessions_json = json.dumps([{
        'id': s.id,
        'student_id': s.student.id,
        'student_name': s.student.name,
        'student_regno': s.student.register_no,
        'status': s.status,
        'violations': s.violations,
        'violation_reasons': s.violation_reasons or ''
    } for s in sessions])
    
    # Add duration property to sessions for template
    for session in sessions:
        if session.ended_at:
            duration = session.ended_at - session.started_at
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            seconds = duration.seconds % 60
            session.duration = f"{hours}h {minutes}m {seconds}s" if hours > 0 else f"{minutes}m {seconds}s"
        else:
            session.duration = 'In Progress'
    
    return render(request, 'admin/sessions.html', {
        'sessions': sessions,
        'sessions_json': sessions_json,
        'all_students': all_students,
        'total_sessions': total_sessions,
        'active_sessions': active_sessions,
        'completed_sessions': completed_sessions,
        'terminated_sessions': terminated_sessions
    })

@staff_member_required
@csrf_exempt
def create_session(request):
    """Create new exam session"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            student = Student.objects.get(id=data['student_id'])
            session = ExamSession(
                student=student,
                status=data.get('status', 'active'),
                violations=data.get('violations', 0),
                violation_reasons=data.get('violation_reasons', '')
            )
            session.save()
            
            return JsonResponse({'success': True, 'session_id': session.id})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@staff_member_required
@csrf_exempt
def update_session(request, session_id):
    """Update exam session"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session = ExamSession.objects.get(id=session_id)
            
            if 'student_id' in data:
                session.student = Student.objects.get(id=data['student_id'])
            if 'status' in data:
                session.status = data['status']
                if data['status'] in ['completed', 'terminated'] and not session.ended_at:
                    session.ended_at = timezone.now()
            if 'violations' in data:
                session.violations = data['violations']
            if 'violation_reasons' in data:
                session.violation_reasons = data['violation_reasons']
            
            session.save()
            
            return JsonResponse({'success': True})
        except ExamSession.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Session not found'}, status=404)
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@staff_member_required
@csrf_exempt
def delete_session(request, session_id):
    """Delete exam session"""
    if request.method == 'POST':
        try:
            session = ExamSession.objects.get(id=session_id)
            session.delete()
            return JsonResponse({'success': True})
        except ExamSession.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Session not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


# Email Verification
def verify_email(request, token):
    """Verify student email"""
    try:
        student = Student.objects.get(email_verification_token=token)
        student.is_email_verified = True
        student.email_verification_token = None
        student.save()
        return render(request, 'email_verified.html', {'student': student})
    except Student.DoesNotExist:
        return render(request, 'email_verification_failed.html')

# Password Reset
def forgot_password_page(request):
    """Forgot password page"""
    return render(request, 'forgot_password.html')

@csrf_exempt
def forgot_password(request):
    """Send password reset email"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            
            try:
                student = Student.objects.get(email=email)
                token = student.generate_password_reset_token()
                
                reset_link = f"http://localhost:8000/reset-password/{token}/"
                subject = '🔒 ExamGuard - Password Reset Request'
                message = f'''Dear {student.name},

We received a request to reset your password for your ExamGuard account.

🔗 Click here to reset your password: {reset_link}

⏰ This link will expire in 1 hour.

If you didn't request this, please ignore this email.

Best regards,
ExamGuard Team
🛡️ Secure Online Exams with AI
'''
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [student.email],
                    fail_silently=False,
                )
                
                return JsonResponse({'success': True, 'message': 'Password reset link sent to your email'})
            except Student.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Email not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

def reset_password_page(request, token):
    """Reset password page"""
    try:
        student = Student.objects.get(
            password_reset_token=token,
            password_reset_expires__gt=timezone.now()
        )
        return render(request, 'reset_password.html', {'token': token})
    except Student.DoesNotExist:
        return render(request, 'reset_password_expired.html')

@csrf_exempt
def reset_password(request):
    """Reset password"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token = data.get('token')
            new_password = data.get('password')
            
            student = Student.objects.get(
                password_reset_token=token,
                password_reset_expires__gt=timezone.now()
            )
            
            student.set_password(new_password)
            student.password_reset_token = None
            student.password_reset_expires = None
            student.save()
            
            return JsonResponse({'success': True, 'message': 'Password reset successful'})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid or expired token'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

# Student Dashboard
def student_dashboard(request):
    """Student dashboard"""
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('index')
    
    try:
        student = Student.objects.get(id=student_id)
        sessions = ExamSession.objects.filter(student=student).order_by('-started_at')
        
        # Calculate stats
        total_sessions = sessions.count()
        completed_sessions = sessions.filter(status='completed').count()
        terminated_sessions = sessions.filter(status='terminated').count()
        total_violations = sessions.aggregate(Sum('violations'))['violations__sum'] or 0
        
        return render(request, 'student_dashboard.html', {
            'student': student,
            'sessions': sessions,
            'total_sessions': total_sessions,
            'completed_sessions': completed_sessions,
            'terminated_sessions': terminated_sessions,
            'total_violations': total_violations
        })
    except Student.DoesNotExist:
        request.session.flush()
        return redirect('index')

# Save Screenshot
@csrf_exempt
def save_screenshot(request):
    """Save violation screenshot"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = request.session.get('session_id')
            student_id = request.session.get('student_id')
            
            if not session_id or not student_id:
                return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=401)
            
            session = ExamSession.objects.get(id=session_id, student_id=student_id)
            
            screenshot = ViolationScreenshot.objects.create(
                session=session,
                screenshot=data.get('screenshot'),
                violation_type=data.get('violation_type')
            )
            
            return JsonResponse({'success': True, 'screenshot_id': screenshot.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False}, status=400)

# Get Timer
@csrf_exempt
def get_timer(request):
    """Get remaining time for exam"""
    session_id = request.session.get('session_id')
    student_id = request.session.get('student_id')
    
    if not session_id or not student_id:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=401)
    
    try:
        session = ExamSession.objects.get(id=session_id, student_id=student_id)
        time_left = session.get_time_left()
        
        return JsonResponse({
            'success': True,
            'time_left': time_left,
            'exam_duration': session.exam_duration
        })
    except ExamSession.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Session not found'}, status=404)


# Custom Error Handlers
def custom_404(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)

def custom_500(request):
    """Custom 500 error page"""
    return render(request, '500.html', status=500)
