# PythonAnywhere Settings Configuration
# Copy these settings to your settings.py file when deploying to PythonAnywhere

# IMPORTANT: Replace 'yourusername' with your actual PythonAnywhere username

import os

DEBUG = False  # MUST be False in production

ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',
    'localhost',
    '127.0.0.1'
]

# ============================================
# STATIC FILES CONFIGURATION
# ============================================

STATIC_ROOT = '/home/yourusername/examguard/exam-eye-detection/backend/staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    '/home/yourusername/examguard/exam-eye-detection/backend/exam/static'
]

# ============================================
# CSRF CONFIGURATION
# ============================================

CSRF_TRUSTED_ORIGINS = [
    'https://yourusername.pythonanywhere.com',
    'http://yourusername.pythonanywhere.com',
]

CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_USE_SESSIONS = False

# ============================================
# CORS CONFIGURATION
# ============================================

CORS_ALLOWED_ORIGINS = [
    'https://yourusername.pythonanywhere.com',
    'http://yourusername.pythonanywhere.com',
]

CORS_ALLOW_CREDENTIALS = True

# ============================================
# DATABASE CONFIGURATION
# ============================================

# Default SQLite database (already configured)
# No changes needed for PythonAnywhere

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/yourusername/examguard/exam-eye-detection/backend/db.sqlite3',
    }
}

# ============================================
# SECURITY SETTINGS
# ============================================

# Generate a new SECRET_KEY for production
# You can generate one at: https://djecrety.ir/
SECRET_KEY = os.environ['SECRET_KEY']  # Set this in PythonAnywhere environment variables

# Session settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# HTTPS security headers
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# ============================================
# MEDIA FILES (if needed)
# ============================================

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/examguard/exam-eye-detection/backend/media'

# ============================================
# LOGGING (Optional - for debugging)
# ============================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/yourusername/examguard/exam-eye-detection/backend/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# ============================================
# INSTRUCTIONS
# ============================================

"""
1. Copy the settings above to your examproject/settings.py file
2. Replace ALL instances of 'yourusername' with your PythonAnywhere username
3. Generate a new SECRET_KEY for production
4. Save the file
5. Run: python manage.py collectstatic --noinput
6. Reload your web app in PythonAnywhere
"""
