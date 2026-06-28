# ExamGuard - Quick Reference Guide

## 🚀 Getting Started (3 Ways)

### Method 1: Fastest (Double-click)
```
START_SERVER.bat
```
Opens: http://localhost:8000

### Method 2: Admin Access
```
ADMIN_LOGIN.bat
```
Opens: http://localhost:8000/admin
Credentials: admin / admin123

### Method 3: Full Check
```
FIX_AND_START.bat
```
Runs checks, migrations, creates admin, starts server

---

## 🔐 Login Credentials

### Admin Panel
- URL: http://localhost:8000/admin
- Username: `admin`
- Password: `admin123`

### Student Portal
- URL: http://localhost:8000
- Register new account or login with existing credentials

---

## 📋 All URLs

| Page | URL | Access |
|------|-----|--------|
| Student Auth | http://localhost:8000 | Public |
| Exam Page | http://localhost:8000/exam/ | Students only |
| Admin Dashboard | http://localhost:8000/admin | Admin only |
| Students Management | http://localhost:8000/admin-api/students/ | Admin only |
| Sessions Management | http://localhost:8000/admin-api/sessions/ | Admin only |
| Violations Report | http://localhost:8000/admin-api/violations/ | Admin only |
| Password Reset | http://localhost:8000/forgot-password/ | Public |
| Test Page | http://localhost:8000/test | Public |

---

## 🎯 Detection Rules

### Rule 1: Multiple Faces ❌
- **Trigger:** More than 1 person detected
- **Action:** Immediate termination
- **Alert:** "Multiple persons detected"

### Rule 2: No Face ⚠️
- **Trigger:** Face not visible for 3 seconds
- **Action:** Warning + sound alert
- **Alert:** "Please keep your face visible"

### Rule 3: Eye Gaze Tracking ⚠️
- **Trigger:** Looking away from screen >2 seconds
- **Action:** 3-warning system
- **Alert:** "Keep your eyes on the screen"
- **Termination:** After 3 warnings

### Rule 4: Head Turn ⚠️
- **Trigger:** Head turned outside camera view
- **Action:** 3-warning system
- **Alert:** "Keep your head facing the camera"
- **Termination:** After 3 warnings

### Rule 5: Looking Down ⚠️
- **Trigger:** Looking very down for 5 seconds
- **Action:** Warning + sound alert
- **Alert:** "Please keep your eyes on the screen"

### Rule 6: Sleep Detection ❌
- **Trigger:** Eyes closed (EAR < 2.5 pixels)
- **Action:** Immediate termination
- **Alert:** "Sleep/drowsiness detected"

---

## 📧 Email Configuration

### Current Setup
- **Service:** Gmail SMTP
- **Host:** smtp.gmail.com
- **Port:** 587
- **TLS:** Enabled
- **From:** examprivate86@gmail.com

### Emails Sent
1. **Student Registration**
   - Welcome email to student
   - Notification to admin

2. **Password Reset**
   - Reset link with 1-hour expiry

### To Change Email
Edit `exam-eye-detection/backend/examproject/settings.py`:
```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'Your Name <your-email@gmail.com>'
```

---

## 🎨 Features Overview

### Student Features
- ✅ Split-screen login/register
- ✅ Password authentication
- ✅ Email notifications
- ✅ Multi-camera support
- ✅ Real-time face detection
- ✅ Eye gaze tracking
- ✅ Sleep detection
- ✅ Violation warnings
- ✅ Session timer
- ✅ Password reset

### Admin Features
- ✅ Dashboard with statistics
- ✅ Student management (CRUD)
- ✅ Session management (CRUD)
- ✅ Violations report
- ✅ Recent activity feed
- ✅ Dark mode toggle
- ✅ Responsive design

### Detection Features
- ✅ Face detection (face-api.js)
- ✅ Facial landmarks (68 points)
- ✅ Eye tracking with beams
- ✅ Gaze direction calculation
- ✅ Head pose estimation
- ✅ Eye aspect ratio (EAR)
- ✅ Multi-person detection
- ✅ Real-time processing

---

## 🔧 Common Tasks

### Create New Admin User
```bash
cd exam-eye-detection\backend
python manage.py createsuperuser
```

### Reset Database
```bash
cd exam-eye-detection\backend
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Check for Errors
```bash
cd exam-eye-detection\backend
python manage.py check
```

### Apply Migrations
```bash
cd exam-eye-detection\backend
python manage.py makemigrations
python manage.py migrate
```

### Collect Static Files
```bash
cd exam-eye-detection\backend
python manage.py collectstatic
```

---

## 🎥 Camera Controls

### Switch Camera
- Use dropdown in exam page
- Automatically detects all cameras
- Smooth switching without page reload

### Camera Permissions
- Browser will ask for camera access
- Click "Allow" to enable detection
- If blocked, check browser settings

### Troubleshooting Camera
1. Check browser permissions
2. Close other apps using camera
3. Refresh page
4. Try different browser

---

## 📊 Admin Dashboard

### Statistics Cards
1. **Total Students** - All registered students
2. **Exam Sessions** - All exam sessions
3. **Active Now** - Currently active sessions
4. **Total Violations** - Sum of all violations

### Quick Actions
- **Manage Students** - Add/edit/delete students
- **Manage Sessions** - View/edit sessions
- **Violations Report** - Detailed violation logs
- **Student Portal** - Go to student login

### Recent Activity
- Last 10 exam sessions
- Status indicators (🟢 Active, ✅ Completed, 🔴 Terminated)
- Time ago display
- Click to view details

---

## 🎨 Dark Mode

### Toggle Dark Mode
- Click sun/moon button (top-right)
- Automatically saves preference
- Works on all pages

### Theme Persistence
- Stored in browser localStorage
- Persists across sessions
- Per-device setting

---

## 🔐 Security Features

### Password Security
- ✅ Hashed with Django's make_password()
- ✅ Never stored in plain text
- ✅ Secure verification with check_password()

### Session Security
- ✅ Session-based authentication
- ✅ 2-hour session timeout
- ✅ Secure logout with session flush

### CSRF Protection
- ✅ CSRF tokens on all forms
- ✅ Trusted origins configured
- ✅ Protection against cross-site attacks

### Access Control
- ✅ Students can only access own data
- ✅ Admin endpoints require staff permission
- ✅ Session validation on exam page

---

## 📱 Responsive Design

### Desktop (>1200px)
- Full dashboard layout
- Side-by-side forms
- Large camera view

### Tablet (768px - 1200px)
- Stacked forms
- Adjusted grid layouts
- Medium camera view

### Mobile (<768px)
- Single column layout
- Touch-friendly buttons
- Optimized camera view

---

## 🐛 Troubleshooting

### Server won't start
```bash
cd exam-eye-detection\backend
python manage.py check
python manage.py migrate
python manage.py runserver
```

### Can't login to admin
- Username: `admin`
- Password: `admin123`
- Run `ADMIN_LOGIN.bat` to recreate

### Camera not working
1. Allow camera permissions in browser
2. Check if camera is in use by another app
3. Try different browser
4. Refresh page

### CSRF errors
- Already fixed in settings.py
- Clear browser cookies
- Try incognito mode

### Email not sending
1. Check internet connection
2. Verify email settings in settings.py
3. Check Gmail app password
4. Look at console for errors

### Face detection not working
1. Check internet connection (needs face-api.js CDN)
2. Wait for models to load
3. Ensure good lighting
4. Position face in camera view

---

## 📦 File Structure

```
c:\mark-1\
├── START_SERVER.bat              # Quick start
├── ADMIN_LOGIN.bat               # Admin access
├── FIX_AND_START.bat            # Full system check
├── README.md                     # Main documentation
├── SYSTEM_VERIFICATION_COMPLETE.md  # Verification report
└── exam-eye-detection\
    └── backend\
        ├── manage.py             # Django management
        ├── db.sqlite3           # Database
        ├── requirements.txt     # Dependencies
        ├── exam\                # Main app
        │   ├── models.py        # Database models
        │   ├── views.py         # View functions
        │   ├── admin.py         # Admin configuration
        │   ├── urls.py          # URL routing
        │   ├── static\          # CSS/JS files
        │   │   ├── darkmode.css
        │   │   └── darkmode.js
        │   └── templates\       # HTML templates
        │       ├── auth.html    # Login/Register
        │       ├── exam.html    # Exam monitoring
        │       ├── index.html   # Legacy login
        │       └── admin\       # Admin templates
        └── examproject\         # Project settings
            ├── settings.py      # Configuration
            ├── urls.py          # Main URL routing
            └── wsgi.py          # WSGI config
```

---

## 🎯 API Endpoints

### Public Endpoints
- `POST /login/` - Student login
- `POST /signup/` - Student registration
- `POST /forgot-password/send/` - Request password reset
- `POST /reset-password/submit/` - Reset password
- `GET /verify-email/<token>/` - Verify email

### Student Endpoints (Requires Login)
- `GET /exam/` - Exam monitoring page
- `POST /violation/` - Log violation
- `POST /logout/` - Logout
- `POST /save-screenshot/` - Save violation screenshot
- `GET /get-timer/` - Get remaining time

### Admin Endpoints (Requires Staff)
- `GET /admin-api/students/` - List students
- `POST /admin-api/students/create/` - Create student
- `POST /admin-api/students/<id>/update/` - Update student
- `POST /admin-api/students/<id>/delete/` - Delete student
- `GET /admin-api/sessions/` - List sessions
- `POST /admin-api/sessions/create/` - Create session
- `POST /admin-api/sessions/<id>/update/` - Update session
- `POST /admin-api/sessions/<id>/delete/` - Delete session
- `GET /admin-api/violations/` - Violations report
- `POST /admin-api/violations/<id>/clear/` - Clear violations

---

## 💡 Tips & Best Practices

### For Students
1. Use good lighting for better face detection
2. Position face in center of camera
3. Keep eyes on screen during exam
4. Don't move head too much
5. Stay alone in the room

### For Admins
1. Monitor active sessions regularly
2. Review violations report
3. Clear false violations if needed
4. Keep student data updated
5. Use dark mode for comfort

### For Developers
1. Check console for errors
2. Use debug panel in exam page
3. Test with different cameras
4. Verify email configuration
5. Keep dependencies updated

---

## 📞 Support

### Documentation
- README.md - Main guide
- SYSTEM_VERIFICATION_COMPLETE.md - Full verification
- QUICK_REFERENCE.md - This file

### Common Issues
- Check troubleshooting section above
- Review console errors
- Verify configuration in settings.py

---

## 🎉 Quick Start Summary

1. **Run:** `START_SERVER.bat`
2. **Open:** http://localhost:8000
3. **Register:** Create new account
4. **Login:** Use your credentials
5. **Exam:** Click "Start Camera & Begin Exam"
6. **Admin:** http://localhost:8000/admin (admin/admin123)

---

**ExamGuard - Secure Online Exams with AI** 🛡️

*Everything you need in one place!*
