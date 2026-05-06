from django.contrib import admin
from .models import Student, ExamSession, Violation

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'register_no', 'email', 'phone', 'college_name', 'created_at']
    search_fields = ['name', 'register_no', 'email']
    list_filter = ['created_at', 'college_name']

@admin.register(ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ['student', 'started_at', 'ended_at', 'status', 'violations']
    search_fields = ['student__name', 'student__register_no']
    list_filter = ['status', 'started_at']
    readonly_fields = ['started_at']

@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = ['session', 'violation_type', 'timestamp', 'description']
    search_fields = ['session__student__name', 'violation_type']
    list_filter = ['violation_type', 'timestamp']
    readonly_fields = ['timestamp']
