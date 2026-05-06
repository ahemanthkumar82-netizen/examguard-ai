from rest_framework import serializers
from .models import Student, ExamSession, Violation

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'email', 'college_name', 'register_no', 'created_at']

class ExamSessionSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    
    class Meta:
        model = ExamSession
        fields = ['id', 'student', 'started_at', 'ended_at', 'status', 'violations', 'violation_reasons']

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ['id', 'session', 'violation_type', 'timestamp', 'description']
