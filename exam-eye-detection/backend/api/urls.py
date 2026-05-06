from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.student_login, name='login'),
    path('violation/', views.log_violation, name='violation'),
    path('logout/', views.end_session, name='logout'),
    path('session/', views.check_session, name='session'),
    path('sessions/', views.get_sessions, name='sessions'),
    path('violations/<int:session_id>/', views.get_violations, name='violations'),
]
