from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mentors/', views.mentors, name='mentors'),
    path('programs/', views.programs, name='programs'),
    path('mentor-profile/<int:mentor_id>/', views.mentor_profile, name='mentor_profile'),
    path('program-details/<int:program_id>/', views.program_details, name='program_details'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('sessions/', views.sessions, name='sessions'),
    path('book-session/', views.book_session, name='book_session'),
    path('my-sessions/', views.my_sessions, name='my_sessions'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('session-history/', views.session_history, name='session_history'),
    path('logout/', views.user_logout, name='logout'), 
]