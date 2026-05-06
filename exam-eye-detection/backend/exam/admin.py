from django.contrib import admin
from django.db.models import Count, Sum
from .models import Student, ExamSession

class CustomAdminSite(admin.AdminSite):
    site_header = 'ExamGuard Administration'
    site_title = 'ExamGuard Admin'
    index_title = 'Dashboard'
    
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['total_students'] = Student.objects.count()
        extra_context['total_sessions'] = ExamSession.objects.count()
        extra_context['active_sessions'] = ExamSession.objects.filter(status='active').count()
        extra_context['total_violations'] = ExamSession.objects.aggregate(Sum('violations'))['violations__sum'] or 0
        extra_context['recent_sessions'] = ExamSession.objects.select_related('student').order_by('-started_at')[:10]
        return super().index(request, extra_context)

admin_site = CustomAdminSite(name='custom_admin')

@admin.register(Student, site=admin_site)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'register_no', 'email', 'phone', 'college_name', 'created_at']
    search_fields = ['name', 'register_no', 'email']
    list_filter = ['created_at', 'college_name']
    list_per_page = 25
    date_hierarchy = 'created_at'

@admin.register(ExamSession, site=admin_site)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ['student', 'started_at', 'ended_at', 'status', 'violations', 'get_duration']
    search_fields = ['student__name', 'student__register_no']
    list_filter = ['status', 'started_at']
    readonly_fields = ['started_at', 'get_duration']
    list_per_page = 25
    date_hierarchy = 'started_at'
    
    def get_duration(self, obj):
        if obj.ended_at:
            duration = obj.ended_at - obj.started_at
            minutes = int(duration.total_seconds() / 60)
            return f"{minutes} min"
        return "Ongoing"
    get_duration.short_description = 'Duration'
