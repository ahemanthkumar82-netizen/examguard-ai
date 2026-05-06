@echo off
echo ========================================
echo Updating Database for Password Feature
echo ========================================
echo.

cd backend

echo Making migrations...
python manage.py makemigrations

echo.
echo Applying migrations...
python manage.py migrate

echo.
echo ========================================
echo Database updated successfully!
echo ========================================
echo.
pause
