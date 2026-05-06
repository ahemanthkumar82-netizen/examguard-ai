# ExamGuard - PythonAnywhere Deployment Guide

## 🚀 Complete Deployment Instructions

### **Step 1: Create PythonAnywhere Account**
1. Go to https://www.pythonanywhere.com
2. Click "Start running Python online in less than a minute!"
3. Choose "Create a Beginner account" (Free)
4. Sign up with email and create password
5. Verify your email

---

### **Step 2: Upload Your Project**

#### **Option A: Upload ZIP File**
1. Create ZIP of `c:\mark-1\exam-eye-detection\backend`
2. Login to PythonAnywhere
3. Click "Files" tab
4. Click "Upload a file"
5. Upload the ZIP file
6. Extract using Bash console

#### **Option B: Use GitHub (Recommended)**
```bash
# In PythonAnywhere Bash console
git clone https://github.com/YOUR_USERNAME/examguard.git
cd examguard/exam-eye-detection/backend
```

---

### **Step 3: Set Up Virtual Environment**

In Bash console:
```bash
cd ~/examguard/exam-eye-detection/backend
mkvirtualenv --python=/usr/bin/python3.10 examguard-env
pip install django
python manage.py collectstatic --noinput
```

---

### **Step 4: Configure Web App**
1. Go to "Web" tab
2. Click "Add a new web app"
3. Click "Next"
4. Choose "Manual configuration"
5. Select "Python 3.10"
6. Click "Next"

---

### **Step 5: Configure WSGI File**

Edit WSGI configuration file with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/examguard/exam-eye-detection/backend'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'examproject.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Replace `yourusername` with your actual PythonAnywhere username!**

---

### **Step 6: Configure Virtual Environment**

In "Web" tab, "Virtualenv" section:
```
/home/yourusername/.virtualenvs/examguard-env
```

---

### **Step 7: Update Django Settings**

See `PYTHONANYWHERE_SETTINGS.py` for required changes.

---

### **Step 8: Set Up Static Files**

In "Web" tab, "Static files" section:
- URL: `/static/`
- Directory: `/home/yourusername/examguard/exam-eye-detection/backend/staticfiles`

---

### **Step 9: Create Database**

```bash
cd ~/examguard/exam-eye-detection/backend
python manage.py migrate
python manage.py createsuperuser
```

Credentials:
- Username: `admin`
- Password: `admin123`

---

### **Step 10: Reload Web App**

Click the green "Reload" button in Web tab.

---

## 🌐 Your Live URLs

- **Student Portal**: https://yourusername.pythonanywhere.com
- **Admin Panel**: https://yourusername.pythonanywhere.com/admin

---

## 📱 Share with Friends

```
🎓 ExamGuard - Online Exam System

📱 Student Portal:
https://yourusername.pythonanywhere.com

👨💼 Admin Panel:
https://yourusername.pythonanywhere.com/admin
Username: admin
Password: admin123

✅ Works on Desktop & Mobile
✅ Camera detection enabled
✅ Real-time monitoring
```

---

## 🔧 Troubleshooting

### Check Error Logs
1. Go to "Web" tab
2. Click "Error log" link
3. Check for errors

### Reload Static Files
```bash
cd ~/examguard/exam-eye-detection/backend
python manage.py collectstatic --noinput
```

### Database Issues
```bash
python manage.py migrate
```

---

## 📊 Free Tier Features

✅ 512 MB disk space
✅ 1 web app
✅ HTTPS enabled
✅ Always accessible
⚠️ Site sleeps after 3 months inactivity

---

## 🔄 Update Site Later

```bash
cd ~/examguard/exam-eye-detection/backend
git pull  # If using GitHub
python manage.py collectstatic --noinput
```

Then click "Reload" in Web tab.

---

## ✅ Deployment Checklist

- [ ] Account created
- [ ] Project uploaded
- [ ] Virtual environment created
- [ ] Django installed
- [ ] Web app configured
- [ ] WSGI file updated
- [ ] Settings.py updated
- [ ] Static files configured
- [ ] Database migrated
- [ ] Admin user created
- [ ] Web app reloaded
- [ ] Site tested

---

**Your ExamGuard system is now live and accessible worldwide!** 🌍
