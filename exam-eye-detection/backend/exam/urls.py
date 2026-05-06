from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_page, name='register'),
    path('exam/', views.exam_page, name='exam'),
    path('login/', views.student_login, name='login'),
    path('signup/', views.student_signup, name='signup'),
    path('violation/', views.log_violation, name='violation'),
    path('logout/', views.logout_view, name='logout'),
    path('test/', TemplateView.as_view(template_name='test.html'), name='test'),
    
    # Email Verification
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),
    
    # Password Reset
    path('forgot-password/', views.forgot_password_page, name='forgot_password_page'),
    path('forgot-password/send/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:token>/', views.reset_password_page, name='reset_password_page'),
    path('reset-password/submit/', views.reset_password, name='reset_password'),
    
    # Student Dashboard
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    
    # Screenshot & Timer
    path('save-screenshot/', views.save_screenshot, name='save_screenshot'),
    path('get-timer/', views.get_timer, name='get_timer'),
    
    # Admin API endpoints
    path('admin-api/students/', views.students_management, name='students_management'),
    path('admin-api/students/create/', views.create_student, name='create_student'),
    path('admin-api/students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('admin-api/students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('admin-api/violations/', views.violations_report, name='violations_report'),
    path('admin-api/violations/<int:session_id>/clear/', views.clear_violations, name='clear_violations'),
    path('admin-api/sessions/', views.sessions_management, name='sessions_management'),
    path('admin-api/sessions/create/', views.create_session, name='create_session'),
    path('admin-api/sessions/<int:session_id>/update/', views.update_session, name='update_session'),
    path('admin-api/sessions/<int:session_id>/delete/', views.delete_session, name='delete_session'),
]
