# 📧 Email Notification Setup Guide

## ✅ Feature Added: Admin Email Notifications

When a new student registers, you'll receive an email at **examprivate86@gmail.com** with complete student details!

---

## 🔧 Setup Gmail for Sending Emails

### **Step 1: Enable 2-Step Verification**

1. Go to https://myaccount.google.com/security
2. Click **"2-Step Verification"**
3. Follow the steps to enable it

### **Step 2: Create App Password**

1. Go to https://myaccount.google.com/apppasswords
2. Select **"Mail"** and **"Windows Computer"**
3. Click **"Generate"**
4. Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)

### **Step 3: Update Django Settings**

Edit `c:\mark-1\exam-eye-detection\backend\examproject\settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'  # Your App Password (16 chars)
DEFAULT_FROM_EMAIL = 'ExamGuard <your-email@gmail.com>'
```

**Replace:**
- `your-email@gmail.com` with your actual Gmail
- `abcd efgh ijkl mnop` with your App Password

### **Step 4: Restart Server**

```bash
cd c:\mark-1
START_SERVER.bat
```

---

## 📧 What Emails Are Sent?

### **1. Admin Notification (to examprivate86@gmail.com)**

When a student registers, you receive:

```
Subject: 🎓 New Student Registration - [Student Name]

Content:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 STUDENT DETAILS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 Full Name:           John Doe
🪪 Register Number:     REG12345
📧 Email Address:       john@example.com
📱 Phone Number:        1234567890
🏫 College/University:  ABC University
📅 Registration Date:   December 20, 2024
⏰ Registration Time:   02:30 PM

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
```

### **2. Welcome Email (to Student)**

Student receives:

```
Subject: 🎓 Welcome to ExamGuard - Account Created Successfully

Content:
Dear [Student Name],

Welcome to ExamGuard! Your account has been created successfully.

📋 Your Account Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Full Name: [Name]
🪪 Register Number: [Regno]
📱 Phone: [Phone]
📧 Email: [Email]
🏫 College: [College]
📅 Account Created: [Date & Time]
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
```

---

## 🧪 Test Email Functionality

### **Create Test Script:** `c:\mark-1\test_email.py`

```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examproject.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

try:
    send_mail(
        'Test Email from ExamGuard',
        'This is a test email. If you receive this, email configuration is working!',
        settings.DEFAULT_FROM_EMAIL,
        ['examprivate86@gmail.com'],
        fail_silently=False,
    )
    print("✅ Test email sent successfully!")
    print("Check examprivate86@gmail.com inbox")
except Exception as e:
    print(f"❌ Error sending email: {e}")
```

### **Run Test:**

```bash
cd c:\mark-1\exam-eye-detection\backend
python test_email.py
```

---

## 🔒 Security Best Practices

### **1. Use App Password (Not Regular Password)**
- Never use your regular Gmail password
- Always use App Password generated from Google

### **2. Keep Credentials Secret**
- Don't commit settings.py with real credentials to GitHub
- Use environment variables for production

### **3. For Production (PythonAnywhere):**

Create `.env` file:
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Update settings.py:
```python
import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

---

## 🎯 Email Notification Flow

```
Student Registers
       ↓
Django Creates Account
       ↓
   ┌───────────────────┐
   │                   │
   ↓                   ↓
Admin Email      Student Email
(examprivate86)  (student's email)
   │                   │
   ↓                   ↓
Full Details     Welcome Message
```

---

## 📊 What You'll Receive

Every time someone registers:
- ✅ Instant email notification
- ✅ Complete student details
- ✅ Registration timestamp
- ✅ Direct links to admin panel
- ✅ Account status confirmation

---

## 🆘 Troubleshooting

### **Email Not Sending?**

1. **Check Gmail Settings:**
   - 2-Step Verification enabled?
   - App Password created?
   - Correct email and password in settings.py?

2. **Check Server Logs:**
   - Look for error messages in terminal
   - Check if `fail_silently=True` is hiding errors

3. **Test SMTP Connection:**
   ```python
   import smtplib
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login('your-email@gmail.com', 'your-app-password')
   print("✅ SMTP connection successful!")
   server.quit()
   ```

4. **Check Spam Folder:**
   - First emails might go to spam
   - Mark as "Not Spam"

### **"Authentication Failed" Error?**

- Double-check App Password (16 characters, no spaces)
- Make sure 2-Step Verification is enabled
- Try generating a new App Password

### **"SMTPException" Error?**

- Check internet connection
- Verify EMAIL_PORT = 587
- Verify EMAIL_USE_TLS = True

---

## 💡 Pro Tips

### **1. Email Formatting:**
The emails use Unicode characters for better formatting:
- ━ (box drawing)
- 🎓 📧 📱 (emojis)
- Makes emails more professional and readable

### **2. Silent Failure:**
Emails use `fail_silently=True` so registration continues even if email fails

### **3. Multiple Recipients:**
To send to multiple admins:
```python
['examprivate86@gmail.com', 'admin2@gmail.com', 'admin3@gmail.com']
```

### **4. HTML Emails (Optional):**
For richer formatting, use `send_html_mail()` instead

---

## ✅ Quick Setup Checklist

- [ ] Enable 2-Step Verification on Gmail
- [ ] Generate App Password
- [ ] Update EMAIL_HOST_USER in settings.py
- [ ] Update EMAIL_HOST_PASSWORD in settings.py
- [ ] Update DEFAULT_FROM_EMAIL in settings.py
- [ ] Restart Django server
- [ ] Test with test_email.py
- [ ] Register a test student
- [ ] Check examprivate86@gmail.com inbox
- [ ] Verify email received with student details

---

## 🎉 You're All Set!

Now whenever a new student registers:
1. Student fills registration form
2. Account is created
3. **You receive email at examprivate86@gmail.com** with all details
4. Student receives welcome email
5. Both can start using ExamGuard!

---

**ExamGuard - Now with Email Notifications!** 📧✅
