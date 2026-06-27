from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, ExamSession, Violation
from .serializers import StudentSerializer, ExamSessionSerializer, ViolationSerializer

def home(request):
    """Homepage view"""
    return render(request, 'home.html')

@api_view(['POST'])
def student_login(request):
    """Student login endpoint"""
    try:
        data = request.data
        try:
            student = Student.objects.get(register_no=data['regno'])
        except Student.DoesNotExist:
            return Response({'success': False, 'error': 'Register number not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Create new exam session
        session = ExamSession.objects.create(student=student)
        
        request.session['student_id'] = student.id
        request.session['session_id'] = session.id
        
        return Response({
            'success': True,
            'student': {
                'id': student.id,
                'name': student.name,
                'regno': student.register_no
            },
            'session_id': session.id
        })
    except Exception as e:
        return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def log_violation(request):
    """Log violation endpoint"""
    try:
        session_id = request.session.get('session_id')
        if not session_id:
            return Response({
                'success': False,
                'error': 'No active session'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        session = ExamSession.objects.get(id=session_id)
        violation_type = request.data.get('violation_type')
        description = request.data.get('description', '')
        
        # Create violation record
        Violation.objects.create(
            session=session,
            violation_type=violation_type,
            description=description
        )
        
        # Update session
        session.violations += 1
        if session.violation_reasons:
            session.violation_reasons += f", {violation_type}"
        else:
            session.violation_reasons = violation_type
        
        # Terminate session if violation occurred
        session.status = 'terminated'
        session.ended_at = timezone.now()
        session.save()
        
        return Response({
            'success': True,
            'violations': session.violations
        })
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def end_session(request):
    """End exam session endpoint"""
    session_id = request.session.get('session_id')
    if session_id:
        try:
            session = ExamSession.objects.get(id=session_id)
            if session.status == 'active':
                session.status = 'completed'
            session.ended_at = timezone.now()
            session.save()
        except ExamSession.DoesNotExist:
            pass
    
    request.session.flush()
    return Response({'success': True})

@api_view(['GET'])
def check_session(request):
    """Check if user has active session"""
    student_id = request.session.get('student_id')
    session_id = request.session.get('session_id')
    
    if student_id and session_id:
        try:
            student = Student.objects.get(id=student_id)
            session = ExamSession.objects.get(id=session_id, student_id=student_id)
            return Response({
                'authenticated': True,
                'student': {
                    'id': student.id,
                    'name': student.name,
                    'regno': student.register_no
                },
                'session': {
                    'id': session.id,
                    'status': session.status,
                    'violations': session.violations
                }
            })
        except (Student.DoesNotExist, ExamSession.DoesNotExist):
            pass

@api_view(['GET'])
def get_sessions(request):
    """Get all exam sessions (admin only)"""
    if not request.user.is_staff:
        return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
    sessions = ExamSession.objects.all().order_by('-started_at')
    serializer = ExamSessionSerializer(sessions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_violations(request, session_id):
    """Get violations for a session (admin only)"""
    if not request.user.is_staff:
        return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
    violations = Violation.objects.filter(session_id=session_id).order_by('-timestamp')
    serializer = ViolationSerializer(violations, many=True)
    return Response(serializer.data)
