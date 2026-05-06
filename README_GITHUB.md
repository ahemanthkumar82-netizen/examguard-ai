# ExamGuard - AI-Powered Online Exam Monitoring System

![ExamGuard](https://img.shields.io/badge/ExamGuard-AI%20Proctoring-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Django](https://img.shields.io/badge/Django-5.2+-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Overview

ExamGuard is a comprehensive AI-powered online exam monitoring system that uses advanced face detection and eye tracking technology to ensure exam integrity. Built with Django and face-api.js, it provides real-time monitoring with beautiful 3D animated interfaces.

## ✨ Features

### 🔐 Authentication & Security
- Two-page authentication system (Login + Registration)
- Password hashing with Django's security
- Session-based authentication
- Student data isolation (students can only access their own data)
- Admin-only pages with role-based access control
- CSRF protection

### 📷 AI Detection System
- **Face Detection** - TinyFaceDetector with 68-point facial landmarks
- **Multiple Person Detection** - Instant termination
- **Eye Gaze Tracking** - 3 warnings before termination
- **Head Turn Detection** - 2 warnings before termination
- **Looking Down Detection** - Strict thresholds with warnings
- **Sleep Detection** - Eye aspect ratio monitoring with sound alerts
- **Camera Blocking Detection** - Automatic detection
- **Multi-camera Support** - Switch between cameras

### 🎨 User Interface
- **3D Parallax Effects** - Mouse-tracking card tilt on login/register
- **Animated Trackers** - Advanced face and eye tracking visualizations
- **Glassmorphism Design** - Modern blur effects
- **Responsive Layout** - Works on all screen sizes
- **Real-time Status** - Live detection status updates

### 👨‍💼 Admin Panel
- **Dashboard** - Statistics with clickable cards
- **Students Management** - Full CRUD operations
- **Sessions Management** - Track all exam sessions
- **Violations Report** - Color-coded severity levels
- **Active Users Monitoring** - See who's taking exams now
- **Real-time Statistics** - Live data updates

### 📧 Email Notifications
- Admin notifications on new registrations
- Student welcome emails
- Complete student details in emails
- Gmail SMTP integration

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Modern web browser with webcam
- Internet connection (for face-api.js CDN)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ahemanthkumar82-netizen/examguard-ai-proctoring.git
cd examguard-ai-proctoring
```

2. **Install dependencies**
```bash
cd exam-eye-detection/backend
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Create admin user**
```bash
python create_admin.py
```

5. **Start the server**
```bash
python manage.py runserver
```

Or simply run:
```bash
START_SERVER.bat
```

### Access URLs

| Page | URL |
|------|-----|
| **Student Login** | http://localhost:8000 |
| **Student Register** | http://localhost:8000/register/ |
| **Exam Page** | http://localhost:8000/exam/ |
| **Admin Dashboard** | http://localhost:8000/admin/ |
| **Students Management** | http://localhost:8000/admin-api/students/ |
| **Sessions Management** | http://localhost:8000/admin-api/sessions/ |
| **Violations Report** | http://localhost:8000/admin-api/violations/ |

### Default Admin Credentials
```
Username: admin
Password: admin123
```

## 📁 Project Structure

```
examguard-ai-proctoring/
├── exam-eye-detection/
│   └── backend/
│       ├── exam/
│       │   ├── models.py          # Database models
│       │   ├── views.py           # View functions
│       │   ├── admin.py           # Admin configuration
│       │   ├── urls.py            # URL routing
│       │   └── templates/
│       │       ├── login.html     # 3D animated login
│       │       ├── register.html  # 3D animated registration
│       │       ├── exam.html      # Face detection page
│       │       └── admin/         # Admin templates
│       ├── examproject/
│       │   ├── settings.py        # Django settings
│       │   └── urls.py            # Main URL config
│       ├── manage.py
│       └── requirements.txt
├── .gitignore
├── README.md
└── Batch files for quick start
```

## 🎯 Detection Rules

1. **Multiple Persons** - Instant termination
2. **No Face** - Warning after 3 seconds
3. **Eye Gaze Away** - 3 warnings, then termination
4. **Head Turn** - 2 warnings, then termination
5. **Looking Down** - Warning after 5 seconds (strict thresholds)
6. **Sleep Detection** - Instant termination with sound alert
7. **Camera Blocked** - Instant termination

## 🛠️ Technology Stack

- **Backend:** Django 5.2+
- **Frontend:** HTML5, CSS3, JavaScript
- **Face Detection:** face-api.js (TinyFaceDetector)
- **Database:** SQLite3
- **Email:** Gmail SMTP
- **Styling:** Custom CSS with animations

## 📧 Email Configuration

Update `examproject/settings.py`:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

See `EMAIL_SETUP_GUIDE.md` for detailed instructions.

## 🌐 Deployment

### PythonAnywhere
See `PYTHONANYWHERE_DEPLOYMENT.md` for complete deployment guide.

### Mobile Access
See `VSCODE_PORT_FORWARDING.md` for accessing on mobile devices.

## 🔒 Security Features

- Password hashing with Django's `make_password()`
- Session-based authentication
- CSRF protection
- Student data isolation
- Admin-only access control
- Secure email configuration

## 📊 Database Models

### Student
- Name, Register Number, Email, Phone, College
- Password (hashed)
- Created timestamp

### ExamSession
- Student (Foreign Key)
- Start/End timestamps
- Status (active/completed/terminated)
- Violations count
- Violation reasons

## 🎨 UI Features

- **3D Parallax Effects** - Mouse-tracking animations
- **Glassmorphism** - Modern blur effects
- **Animated Gradients** - Smooth color transitions
- **Floating Particles** - Dynamic background elements
- **Scanning Effects** - Face tracker animations
- **Pulsing Indicators** - Eye tracking visualizations

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Hemanth Kumar**
- GitHub: [@ahemanthkumar82-netizen](https://github.com/ahemanthkumar82-netizen)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please open an issue on GitHub.

## 🙏 Acknowledgments

- face-api.js for face detection library
- Django community for the amazing framework
- All contributors and testers

---

**ExamGuard - Secure Online Exams with AI** 🛡️
