# ExamGuard - New Login System

## ✅ Dynamic Login Added!

### Flow:

```
1. Login Page (/) 
   ↓
   Register Number + Password
   ↓
   ✅ Login → Exam Page
   
   OR
   
   📝 New Student? Register
   ↓
2. Register Page (/register/)
   ↓
   Name, Phone, Email, College, Regno, Password
   ↓
   ✅ Register → Exam Page
```

---

## Pages:

### 1. Login Page (Default - `/`)
- **Fields:**
  - 🪪 Register Number
  - 🔑 Password (with show/hide button 👁️)
- **Features:**
  - Password toggle
  - Link to register page
  - Error messages
  - Violation warnings

### 2. Register Page (`/register/`)
- **Fields:**
  - 👤 Full Name
  - 📱 Phone Number
  - 📧 Email ID
  - 🏫 College Name
  - 🪪 Register Number
  - 🔑 Password (with show/hide button 👁️)
- **Features:**
  - Password toggle
  - Link back to login
  - Auto-login after registration

### 3. Exam Page (`/exam/`)
- Face detection
- Eye tracking
- Violation monitoring

---

## How It Works:

### For New Students:
1. Go to http://localhost:8000
2. Click "📝 New Student? Register Here"
3. Fill all details + create password
4. Click "✅ Register & Start Exam"
5. Automatically logged in → Exam starts

### For Existing Students:
1. Go to http://localhost:8000
2. Enter Register Number
3. Enter Password
4. Click "🚀 Login"
5. Exam starts

---

## Password Features:

- ✅ Stored securely (hashed)
- ✅ Show/hide toggle (👁️/🙈)
- ✅ Required for login
- ✅ Set during registration

---

## API Endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Login page |
| `/register/` | GET | Register page |
| `/login/` | POST | Login with regno + password |
| `/signup/` | POST | Register new student |
| `/exam/` | GET | Exam monitoring page |

---

## To Start:

```bash
cd c:\mark-1\exam-eye-detection\backend
python manage.py runserver
```

Then visit: **http://localhost:8000**

---

## Test Flow:

1. **Register a student:**
   - Go to http://localhost:8000
   - Click "New Student? Register Here"
   - Fill: Name, Phone, Email, College, Regno, Password
   - Submit

2. **Login:**
   - Go to http://localhost:8000
   - Enter Regno + Password
   - Login

3. **Exam:**
   - Face detection starts
   - Follow rules
   - Complete exam

---

## All Working! ✅

- Dynamic login page first
- Register page for new students
- Password authentication
- Secure password storage
- Show/hide password toggle
- Clean navigation between pages

**ExamGuard - Secure & Dynamic!** 🚀
