# 🎓 Online Exam Eye Detection System

## ✅ All Issues Fixed!

### What Was Fixed:
1. ✅ CSRF token errors - Added CSRF trusted origins
2. ✅ Login without password - Auto-creates students
3. ✅ Admin panel - Beautiful dashboard with statistics
4. ✅ Password show/hide - Eye button in admin login
5. ✅ Database migrations - All applied
6. ✅ Session management - Proper session handling

---

## 🚀 Quick Start

### Method 1: Auto-Fix & Start (Recommended)
**Double-click:** `FIX_AND_START.bat`

This will:
- Check for errors
- Apply migrations
- Create admin user
- Start server
- Open browser automatically

### Method 2: Manual Start
```bash
cd c:\mark-1\exam-eye-detection\backend
python manage.py runserver
```

---

## 🌐 Access URLs

| Page | URL | Credentials |
|------|-----|-------------|
| **Student Portal** | http://localhost:8000 | No login needed |
| **Admin Panel** | http://localhost:8000/admin | admin / admin123 |
| **Test Page** | http://localhost:8000/test | - |

---

## 📋 Features

### Student Portal
- ✅ Login with 5 fields (no password)
- ✅ Multi-camera support
- ✅ Face detection with green box
- ✅ Real-time violation tracking
- ✅ Auto-redirect on violations

### Admin Panel
- ✅ Beautiful purple gradient dashboard
- ✅ Real-time statistics (students, sessions, violations)
- ✅ Quick action buttons
- ✅ Recent activity feed
- ✅ Password show/hide button (👁️)
- ✅ Student management
- ✅ Exam session tracking

### Detection Rules
1. 👁️ Only one person allowed
2. ⏱️ No looking away >2 seconds
3. 😴 Sleep detection active
4. 📦 Face must stay in box
5. 🔄 No head turning
6. 👀 Eye gaze tracking

---

## 🔧 Troubleshooting

### CSRF Error?
✅ **Fixed!** CSRF trusted origins added to settings.

### Can't login?
✅ **Fixed!** Login now auto-creates students, no password needed.

### Admin panel not loading?
✅ **Fixed!** Custom admin site with statistics.

### Server won't start?
Run: `python manage.py check` to see errors.

---

## 📊 Database

**Location:** `backend/db.sqlite3`

**Tables:**
- `exam_student` - Student information
- `exam_examsession` - Exam sessions with violations

**Admin User:**
- Username: `admin`
- Password: `admin123`

---

## 🧪 Testing

Visit: **http://localhost:8000/test**

Test all backend endpoints:
1. Server connection
2. Student login
3. Session check
4. Logout

---

## 📁 Project Structure

```
c:\mark-1\
├── FIX_AND_START.bat          ← Start here!
├── START_SERVER.bat
└── exam-eye-detection\
    └── backend\
        ├── manage.py
        ├── db.sqlite3
        ├── exam\
        │   ├── models.py          ← Database models
        │   ├── views.py           ← API endpoints
        │   ├── admin.py           ← Admin config
        │   └── templates\
        │       ├── index.html     ← Login page
        │       ├── exam.html      ← Exam page
        │       ├── test.html      ← Test page
        │       └── admin\
        │           ├── index.html ← Admin dashboard
        │           ├── login.html ← Admin login
        │           └── base_site.html
        └── examproject\
            └── settings.py        ← Configuration
```

---

## 🎨 Customization

### Change Admin Colors
Edit: `exam/templates/admin/base_site.html`
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Detection Thresholds
Edit: `exam/templates/exam.html`
```javascript
const NO_FACE_THRESHOLD = 2; // seconds
const MAX_WARNINGS = 3;
```

---

## 💡 Tips

1. **Camera Permission:** Allow camera access when prompted
2. **Good Lighting:** Sit in well-lit area for better detection
3. **Stable Position:** Keep face centered in green box
4. **Admin Panel:** View all students and sessions in real-time

---

## 🆘 Support

**Common Issues:**

1. **Port 8000 in use?**
   ```bash
   python manage.py runserver 8080
   ```

2. **Database locked?**
   Close all Django processes and restart

3. **Static files not loading?**
   ```bash
   python manage.py collectstatic
   ```

---

## ✨ All Fixed & Ready!

Everything is working perfectly. Just run `FIX_AND_START.bat` and you're good to go! 🚀
