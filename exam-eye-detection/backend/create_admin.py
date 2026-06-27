import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examproject.settings')
django.setup()

from django.contrib.auth.models import User

username = os.environ.get('ADMIN_USERNAME', 'admin')
email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
password = os.environ.get('ADMIN_PASSWORD')

if not password:
    print('Error: ADMIN_PASSWORD environment variable is required.')
    exit(1)

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Admin user "{username}" created successfully.')
else:
    print(f'Admin user "{username}" already exists.')
