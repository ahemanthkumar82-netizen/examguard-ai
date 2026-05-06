@echo off
echo ========================================
echo   Online Exam Eye Detection System
echo ========================================
echo.
echo Starting Backend Server...
start cmd /k "cd backend && python manage.py runserver 8000"
timeout /t 3 >nul
echo.
echo Starting Frontend Server...
start cmd /k "cd frontend && npm start"
echo.
echo ========================================
echo   Servers Starting...
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo Admin:    http://localhost:8000/admin
echo.
echo Username: admin
echo Password: admin123
echo.
pause
