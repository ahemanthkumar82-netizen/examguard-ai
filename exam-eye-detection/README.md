# 🎓 Online Exam Eye Detection System

A complete real-time eye and face detection system for online exams using **Django (Backend)** and **React.js (Frontend)**.

## ✨ Features

### 🔒 Detection Rules (All Working!)
- ✅ **Only one person allowed** - Multiple faces = Instant redirect
- 👁️ **Face detection** - No face for 2+ seconds = Redirect to login
- 😴 **Sleep detection** - Eyes closed = Sound alert + Redirect
- 📦 **Box boundary** - Face outside detection box = Redirect
- 🔄 **Head turn detection** - Head turned away = Redirect
- ⏱️ **Looking down** - Looking down >2 seconds = Redirect
- 📷 **All system cameras supported**

### 🎯 System Features
- Real-time face tracking with green markers
- Eye tracking with gaze direction visualization (blue markers)
- Live timer showing exam duration
- Violation logging and tracking
- Admin panel for monitoring sessions
- Debug panel showing detection status
- Responsive design with emojis
- Sound alerts for violations

## 🛠️ Tech Stack

### Backend
- Django 4.2.7
- SQLite Database
- Session Management
- CSRF Protection

### Frontend
- React.js 19.2.5
- face-api.js 0.22.2
- Axios for API calls
- CSS3 for styling

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. **Navigate to backend:**
```bash
cd backend
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create admin user:**
```bash
python create_admin.py
```

### Frontend Setup

1. **Navigate to frontend:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

## 🚀 Running the Application

### Option 1: Start Everything (Easiest)
Double-click `START_ALL.bat` - This starts both backend and frontend!

### Option 2: Start Separately

**Backend:**
```bash
cd backend
python manage.py runserver 8000
```
Or double-click `START_BACKEND.bat`

**Frontend:**
```bash
cd frontend
npm start
```
Or double-click `START_FRONTEND.bat`

## 🌐 Access Points

- **Frontend (Student):** http://localhost:3000
- **Backend API:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

## 🔐 Admin Credentials

**Username:** `admin`  
**Password:** `admin123`

## 📊 Project Structure

```
exam-eye-detection/
├── backend/
│   ├── examproject/          # Django project settings
│   ├── exam/                 # Main app
│   │   ├── models.py         # Student, ExamSession models
│   │   ├── views.py          # API views
│   │   ├── urls.py           # URL routing
│   │   ├── admin.py          # Admin configuration
│   │   └── templates/        # Django templates (backup)
│   ├── manage.py
│   ├── db.sqlite3
│   ├── create_admin.py       # Admin user creation script
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js      # Login page
│   │   │   ├── Login.css
│   │   │   ├── ExamPage.js   # Exam monitoring page
│   │   │   └── ExamPage.css
│   │   ├── App.js            # Main app component
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── README.md
├── START_ALL.bat             # Start both servers
├── START_BACKEND.bat         # Start backend only
├── START_FRONTEND.bat        # Start frontend only
└── README.md                 # This file
```

## 🎮 How to Use

### For Students:

1. **Open** http://localhost:3000
2. **Fill in** your details:
   - Full Name
   - Phone Number (10 digits)
   - Email ID
   - College Name
   - Register Number
3. **Click** "🚀 Start Exam"
4. **Click** "📷 Start Camera & Begin Exam"
5. **Follow the rules** - Stay in frame, don't look away!

### For Admins:

1. **Open** http://localhost:8000/admin
2. **Login** with admin credentials
3. **View** all students, sessions, and violations
4. **Monitor** exam activity in real-time

## 🔍 Detection Features Explained

### 1. Multiple Person Detection
- Detects if more than one face appears
- Instant redirect to login

### 2. No Face Detection
- Tracks when no face is visible
- Countdown timer shows remaining time
- Redirects after 2 seconds

### 3. Sleep Detection
- Monitors eye closure
- Plays sound alert
- Redirects if eyes remain closed

### 4. Box Boundary Detection
- Green box shows detection area
- Redirects if face moves outside

### 5. Head Turn Detection
- Tracks head orientation
- Redirects if head turns away from camera

### 6. Looking Down Detection
- Monitors downward gaze
- Countdown timer shows remaining time
- Redirects after 2 seconds

## 🐛 Debug Panel

Bottom-left corner shows real-time status:
- Camera loading status
- Number of faces detected
- Violation warnings
- Detection errors

## 📝 API Endpoints

- `POST /login/` - Student login
- `POST /violation/` - Log violation
- `POST /logout/` - End session
- `GET /admin/` - Admin panel

## 🎨 Visual Indicators

- **Green Box** - Face detected correctly
- **Red Box** - No face detected
- **Green Dots** - Face tracking points
- **Blue Circles** - Eye tracking
- **Yellow Dot** - Gaze direction endpoint
- **Blue Line** - Gaze direction

## ⚠️ Troubleshooting

### Camera not working?
- Allow camera permissions in browser
- Check if another app is using the camera
- Try selecting a different camera from dropdown

### Backend connection error?
- Make sure backend is running on port 8000
- Check if Django server started successfully
- Verify CORS settings in Django

### Face detection not working?
- Ensure good lighting
- Face the camera directly
- Wait for models to load (check debug panel)
- Check browser console for errors

## 🔒 Security Features

- Session management
- Violation logging
- Automatic session termination
- Admin authentication
- CSRF protection

## 📈 Future Enhancements

- [ ] Multiple exam questions
- [ ] Timer-based exams
- [ ] Screenshot capture on violations
- [ ] Email notifications
- [ ] Advanced analytics dashboard
- [ ] Mobile app support

## 🤝 Contributing

This is a complete working system. Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is for educational purposes.

## 👨‍💻 Support

For issues or questions:
1. Check the debug panel
2. Review browser console
3. Check Django server logs
4. Verify all dependencies are installed

---

**Created with ❤️ for secure online examinations**

🎓 Happy Examining! 🎓
