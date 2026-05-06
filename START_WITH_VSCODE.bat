@echo off
echo ========================================
echo ExamGuard - VS Code Port Forwarding
echo ========================================
echo.
echo Opening VS Code...
cd exam-eye-detection\backend
code .
echo.
echo ========================================
echo INSTRUCTIONS:
echo ========================================
echo.
echo 1. In VS Code terminal (Ctrl + `), run:
echo    python manage.py runserver
echo.
echo 2. VS Code will detect port 8000
echo    Click "Forward Port" notification
echo    OR press Ctrl+Shift+P and type "Forward a Port"
echo.
echo 3. In PORTS panel (bottom of VS Code):
echo    Right-click on port 8000
echo    Select "Port Visibility" -^> "Public"
echo.
echo 4. Copy the Forwarded Address URL
echo    Example: https://abc123-8000.app.github.dev
echo.
echo 5. Open that URL on your phone or share with friends!
echo.
echo ========================================
echo BENEFITS:
echo ========================================
echo - Works from anywhere (not just same WiFi)
echo - HTTPS secure (no browser warnings)
echo - Easy to share
echo - No firewall issues
echo ========================================
echo.
pause
