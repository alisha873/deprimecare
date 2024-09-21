from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mental-health/', views.mental_health, name='mental_health'),
    path('college-counselor/', views.college_counselor, name='college_counselor'),
    path('self-help/', views.self_help, name='self_help'),
    path('about-us/', views.about_us, name='about_us'),
]
