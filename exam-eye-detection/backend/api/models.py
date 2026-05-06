from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    college_name = models.CharField(max_length=200)
    register_no = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return f"{self.student.name} - {self.started_at}"

class Violation(models.Model):
    VIOLATION_TYPES = [
        ('no_face', 'No Face Detected'),
        ('multiple_faces', 'Multiple Faces'),
        ('head_turn', 'Head Turned Outside'),
        ('looking_down', 'Looking Down'),
        ('sleep', 'Sleep Detected'),
        ('out_of_box', 'Out of Detection Box'),
        ('camera_blocked', 'Camera Blocked'),
    ]
    
    session = models.ForeignKey(ExamSession, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=20, choices=VIOLATION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.session.student.name} - {self.violation_type} - {self.timestamp}"
