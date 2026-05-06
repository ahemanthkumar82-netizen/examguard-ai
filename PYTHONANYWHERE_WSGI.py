# WSGI Configuration for PythonAnywhere
# Copy this entire file content to your WSGI configuration file in PythonAnywhere

# ============================================
# IMPORTANT: Replace 'yourusername' with your actual PythonAnywhere username
# ============================================

import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/examguard/exam-eye-detection/backend'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'examproject.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# ============================================
# HOW TO USE THIS FILE
# ============================================

"""
1. Login to PythonAnywhere
2. Go to "Web" tab
3. Click on your WSGI configuration file link
   (e.g., /var/www/yourusername_pythonanywhere_com_wsgi.py)
4. DELETE all existing content
5. COPY and PASTE this entire file content
6. REPLACE 'yourusername' with your actual PythonAnywhere username
7. Click "Save"
8. Click "Reload" button to restart your web app
"""
