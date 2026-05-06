@echo off
cls
echo ========================================
echo   ExamGuard - Admin Login
echo ========================================
echo.
echo Starting server...
echo.

cd exam-eye-detection\backend

echo Checking admin user...
python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.filter(username='admin').first(); print('Admin exists') if u else User.objects.create_superuser('admin', 'admin@exam.com', 'admin123')"

echo.
echo ========================================
echo   READY!
echo ========================================
echo.
echo Admin Login: http://localhost:8000/admin
echo.
echo Username: admin
echo Password: admin123
echo.
echo Opening browser...
echo ========================================
echo.

start http://localhost:8000/admin

python manage.py runserver
pause
