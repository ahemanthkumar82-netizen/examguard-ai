# ExamGuard - Eye Detection System

## Complete & Ready to Use!

### What is ExamGuard?
ExamGuard is an AI-powered online exam monitoring system that uses eye detection and face tracking to ensure exam integrity.

---

## Quick Start

### Option 1: Double-click
- `START_SERVER.bat` - Start the system
- `ADMIN_LOGIN.bat` - Start & open admin panel
- `FIX_AND_START.bat` - Fix issues & start

### Option 2: Manual
```bash
cd c:\mark-1\exam-eye-detection\backend
python manage.py runserver
```

---

## Access URLs

| Page | URL |
|------|-----|
| **Student Portal** | http://localhost:8000 |
| **Admin Panel** | http://localhost:8000/admin |
| **Test Page** | http://localhost:8000/test |

---

## Admin Credentials

```
Username: admin
Password: admin123
```

---

## Features

### Student Portal
- Login with 5 fields (no password required)
- Multi-camera support
- Real-time face detection
- Eye gaze tracking
- Sleep detection with sound alert
- Automatic violation tracking

### Admin Panel
- Beautiful purple gradient dashboard
- Real-time statistics
- Student management
- Exam session tracking
- Violation reports
- Password show/hide button

### Detection Rules
1. Only one person allowed
2. No looking away >2 seconds
3. Sleep detection active
4. Face must stay visible
5. Head turn detection
6. Eye gaze tracking

---

## System Requirements

- Python 3.8+
- Django 5.2+
- Modern web browser with webcam
- Internet connection (for face-api.js)

---

## Project Structure

```
c:\mark-1\
├── START_SERVER.bat
├── ADMIN_LOGIN.bat
├── FIX_AND_START.bat
└── exam-eye-detection\
    └── backend\
        ├── manage.py
        ├── db.sqlite3
        ├── exam\
        │   ├── models.py
        │   ├── views.py
        │   ├── admin.py
        │   └── templates\
        │       ├── index.html (Student Login)
        │       ├── exam.html (Exam Page)
        │       └── admin\
        │           ├── login.html
        │           ├── index.html
        │           └── base_site.html
        └── examproject\
            └── settings.py
```

---

## Troubleshooting

### Server won't start?
Run: `python manage.py check`

### Can't login to admin?
Use: `admin` / `admin123`

### Camera not working?
Allow camera permissions in browser

### CSRF errors?
Already fixed in latest version

---

## All Features Working

- Student login
- Face detection
- Eye tracking
- Sleep detection
- Multi-camera support
- Admin dashboard
- Violation logging
- Session management
- Password toggle
- Responsive design

---

## Ready to Use!

Just run `START_SERVER.bat` and open http://localhost:8000

**ExamGuard - Secure Online Exams with AI**
