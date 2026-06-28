# ExamGuard - AI Proctoring System

## 🚀 Complete & Ready to Use!

### What is ExamGuard?
ExamGuard is an advanced AI-powered online exam monitoring system featuring futuristic face detection, eye gaze tracking, and intelligent violation detection to ensure exam integrity.

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
| **Login Page** | http://localhost:8000/login |
| **Register Page** | http://localhost:8000/register |
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
- Modern blue/cyan gradient login page
- Separate register page with password strength meter
- Secure password authentication
- Email notifications on registration
- Multi-camera support with dropdown
- **Futuristic face detection** with neon green corner brackets
- **Electric blue eye trackers** with pulsing glow
- **Animated gaze beam** with particle effects
- Facial mesh overlay with scanning line
- Sleep detection with sound alert
- Intelligent 3-warning system
- Password reset via email
- Dark mode toggle
- Mobile responsive design

### Admin Panel
- Beautiful purple gradient dashboard
- Real-time statistics
- Student management
- Exam session tracking
- Violation reports with reasons
- Password show/hide button

### Detection Rules (Updated)

| Rule | Type | Delay | Cooldown | Action |
|------|------|-------|----------|--------|
| **1. Multiple Faces** | Instant | 0s | - | ❌ Terminate |
| **2. No Face Visible** | Warning | 3s | - | ⚠️ Alert only |
| **3. Eye Gaze Away** | 3-Warning | 3s | 5s | ❌ Terminate at 3 |
| **4. Head Turn** | 3-Warning | 3s | 5s | ❌ Terminate at 3 |
| **5. Looking Down** | Warning | 5s | - | ⚠️ Alert only |
| **6. Sleep/Drowsy** | Instant | 0s | - | ❌ Terminate |

**Warning System:**
- Unified counter: Max 3 warnings total (gaze + head turn combined)
- 5-second cooldown between warnings prevents spam
- Warnings require sustained violation (3-5 seconds)
- Each violation tracked separately but counted together

**Detection Thresholds:**
- Eye Gaze: 80% horizontal, 70% vertical tolerance
- Head Turn: 35% of face width
- Sleep: Eye height <1.8 pixels
- Looking Down: Nose >50px below eyes + Chin >60px below nose

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
├── README.md
├── .gitignore
└── exam-eye-detection\
    └── backend\
        ├── manage.py
        ├── db.sqlite3
        ├── exam\
        │   ├── models.py
        │   ├── views.py
        │   ├── admin.py
        │   ├── urls.py
        │   ├── static\
        │   │   ├── darkmode.css
        │   │   └── darkmode.js
        │   └── templates\
        │       ├── login.html (Blue/Cyan Theme)
        │       ├── register.html
        │       ├── exam.html (Futuristic Tracker)
        │       ├── student_dashboard.html
        │       ├── forgot_password.html
        │       ├── reset_password.html
        │       ├── 404.html
        │       ├── 500.html
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
1. Allow camera permissions in browser
2. Check if camera is connected
3. Try different camera from dropdown
4. Hard refresh: `Ctrl + Shift + R`

### CSRF errors?
Already fixed in latest version

### Futuristic tracker not showing?
1. Hard refresh: `Ctrl + Shift + R`
2. Clear browser cache
3. Restart server

### False violation warnings?
All thresholds optimized with cooldown timers

---

## All Features Working

✅ Student login/register with password  
✅ Email notifications (welcome & admin alerts)  
✅ Password reset functionality  
✅ **Futuristic face detection** (neon green corners)  
✅ **Electric blue eye trackers** (pulsing glow)  
✅ **Animated gaze beam** (particle effects)  
✅ Facial mesh overlay with scanning line  
✅ Enhanced webcam quality (brightness/contrast)  
✅ Intelligent 3-warning system  
✅ Sleep detection (eye aspect ratio)  
✅ Multi-camera support  
✅ Admin dashboard with statistics  
✅ Violation logging with reasons  
✅ Session management  
✅ Password toggle  
✅ Dark mode support  
✅ Mobile responsive design  
✅ Blue/cyan login theme  
✅ Camera error handling (no redirect)  

---

## Latest Updates (v2.0)

### Futuristic Tracker
- Neon green corner brackets (not square box)
- Facial mesh overlay (15% opacity)
- Electric blue eye trackers with glow
- Animated gaze beam with particles
- Pulsing target rings
- Smooth interpolation
- Scanning line animation

### Fixed Violations
- Unified warning counter (max 3 total)
- 5-second cooldown between warnings
- 3-second delay before triggering
- Less sensitive thresholds (80% gaze, 35% head turn)
- No false positives
- Proper timer resets

### Camera Improvements
- Error alerts instead of redirect
- Enhanced video quality filters
- Better face detection (40% threshold)
- Optimized for all face types

---

## Ready to Use!

Just run `START_SERVER.bat` and open http://localhost:8000

**ExamGuard v2.0 - Secure Online Exams with AI**
