from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
import uuid
from datetime import timedelta

class Student(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    college_name = models.CharField(max_length=200)
    register_no = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, blank=True, null=True)
    password_reset_token = models.CharField(max_length=100, blank=True, null=True)
    password_reset_expires = models.DateTimeField(blank=True, null=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def generate_verification_token(self):
        self.email_verification_token = str(uuid.uuid4())
        self.save()
        return self.email_verification_token
    
    def generate_password_reset_token(self):
        self.password_reset_token = str(uuid.uuid4())
        self.password_reset_expires = timezone.now() + timedelta(hours=1)
        self.save()
        return self.password_reset_token

    def __str__(self):
        return f"{self.name} - {self.register_no}"

class ExamSession(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('terminated', 'Terminated'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    violations = models.IntegerField(default=0)
    violation_reasons = models.TextField(blank=True)
    exam_duration = models.IntegerField(default=60)  # minutes
    time_remaining = models.IntegerField(null=True, blank=True)  # seconds
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.started_at}"
    
    def get_time_left(self):
        if self.ended_at:
            return 0
        elapsed = (timezone.now() - self.started_at).total_seconds()
        total_seconds = self.exam_duration * 60
        remaining = max(0, total_seconds - elapsed)
        return int(remaining)

class ViolationScreenshot(models.Model):
    session = models.ForeignKey(ExamSession, on_delete=models.CASCADE)
    screenshot = models.TextField()  # Base64 encoded image
    violation_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.session.student.name} - {self.violation_type} - {self.timestamp}"
