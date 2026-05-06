@echo off
echo ========================================
echo Restarting VizionX Servers
echo ========================================
echo.

echo Stopping existing servers...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM node.exe 2>nul
timeout /t 2 /nobreak >nul

echo.
echo Starting Django Backend Server...
start "Django Backend" cmd /k "cd backend && python manage.py runserver"

echo Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo.
echo Starting React Frontend Server...
start "React Frontend" cmd /k "cd frontend && npm start"

echo.
echo ========================================
echo Both servers are starting!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo ========================================
echo.
echo You can close this window now.
pause
