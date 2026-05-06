# ExamGuard - Student Data Security

## Security Measures Implemented

### 1. Session-Based Authentication
- Each student gets a unique session ID upon login
- Session stores only `student_id` and `session_id`
- Sessions expire when browser closes or logout

### 2. Data Access Control

#### Students CANNOT:
- ❌ View other students' details
- ❌ Access other students' exam sessions
- ❌ Modify other students' violation logs
- ❌ See admin panel or admin data
- ❌ Access student management pages
- ❌ View violations report
- ❌ Access sessions management

#### Students CAN ONLY:
- ✅ View their own exam page
- ✅ Log violations for their own session
- ✅ Logout their own session
- ✅ Register new account
- ✅ Login with their credentials

### 3. Security Checks in Code

#### exam_page() - Line 18
```python
# Only logged-in student can access
student_id = request.session.get('student_id')
if not student_id:
    return redirect('index')

# Only returns logged-in student's data
student = Student.objects.get(id=student_id)
```

#### log_violation() - Line 85
```python
# Verify student is logged in
if not session_id or not student_id:
    return JsonResponse({'error': 'Unauthorized'}, status=401)

# Verify session belongs to logged-in student
session = ExamSession.objects.get(id=session_id, student_id=student_id)
```

#### logout_view() - Line 115
```python
# Verify session belongs to logged-in student
session = ExamSession.objects.get(id=session_id, student_id=student_id)
```

### 4. Admin-Only Access

All admin pages protected with `@staff_member_required`:
- `/admin-api/students/` - Students management
- `/admin-api/sessions/` - Sessions management
- `/admin-api/violations/` - Violations report
- `/admin/` - Django admin panel

### 5. Password Security
- Passwords hashed using Django's `make_password()`
- Never stored in plain text
- Verified using `check_password()`

### 6. Database-Level Security
- Each query filters by `student_id` from session
- No direct database access for students
- All queries use Django ORM with proper filtering

### 7. URL Protection
Students cannot access:
- `/admin/` - Requires staff login
- `/admin-api/*` - All admin API endpoints protected
- Other students' data - Session verification required

## How It Works

### Student Login Flow:
1. Student enters regno + password
2. System verifies credentials
3. Creates exam session
4. Stores `student_id` and `session_id` in session
5. Student can only access their own data

### Data Access Flow:
1. Student makes request
2. System checks session for `student_id`
3. Queries database with `student_id` filter
4. Returns only that student's data
5. Other students' data never exposed

### Security Verification:
```python
# Every student action verifies ownership
session = ExamSession.objects.get(
    id=session_id,           # From session
    student_id=student_id    # From session - ensures ownership
)
```

## Testing Security

### Test 1: Try accessing another student's session
```javascript
// This will FAIL - returns 403 Forbidden
fetch('/violation/', {
    method: 'POST',
    body: JSON.stringify({
        session_id: 999,  // Another student's session
        reason: 'test'
    })
})
```

### Test 2: Try accessing admin pages
```
http://localhost:8000/admin-api/students/
// Redirects to admin login - students cannot access
```

### Test 3: Try viewing other student data
```python
# In exam_page view - only returns logged-in student
student = Student.objects.get(id=student_id)  # From session only
```

## Summary

✅ **Students are completely isolated**
- Each student can only see and modify their own data
- Session-based authentication ensures data ownership
- Database queries always filter by logged-in student ID
- Admin pages require staff authentication
- Passwords are encrypted and secure

✅ **No data leakage possible**
- No API endpoints expose other students' data
- All queries verify session ownership
- Unauthorized access returns 401/403 errors
- Sessions flush on logout

✅ **Admin has full control**
- Only admins can view all students
- Only admins can manage sessions
- Only admins can see violations report
- Protected by Django's staff authentication

---

**ExamGuard - Secure by Design**
