@echo off
cls
echo ========================================
echo   ExamGuard - System Check
echo ========================================
echo.

cd exam-eye-detection\backend

echo [1/5] Checking for errors...
python manage.py check
if %errorlevel% neq 0 (
    echo Errors found!
    pause
    exit /b 1
)
echo No errors found
echo.

echo [2/5] Applying migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo Migration failed!
    pause
    exit /b 1
)
echo Migrations applied
echo.

echo [3/5] Collecting static files...
python manage.py collectstatic --noinput --clear 2>nul
echo Static files ready
echo.

echo [4/5] Creating superuser (if needed)...
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@exam.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin exists')"
echo Admin user ready
echo.

echo [5/5] Starting server...
echo.
echo ========================================
echo   ExamGuard - Ready!
echo ========================================
echo.
echo Opening: http://localhost:8000
echo Admin: http://localhost:8000/admin
echo    Username: admin
echo    Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

start http://localhost:8000

python manage.py runserver
pause
