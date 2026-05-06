@echo off
cls
echo ========================================
echo   ExamGuard - Eye Detection System
echo ========================================
echo.
echo Starting Django Server...
echo.
cd exam-eye-detection\backend
python manage.py runserver
pause
