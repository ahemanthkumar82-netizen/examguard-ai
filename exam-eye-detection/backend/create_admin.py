import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examproject.settings')
django.setup()

from django.contrib.auth.models import User

# Create admin user
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Admin user created successfully!')
    print(f'Username: {username}')
    print(f'Password: {password}')
else:
    print('Admin user already exists!')
    print(f'Username: {username}')
    print(f'Password: {password}')
