from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('SignUp/', views.sign_up , name='SignUp'),
    path('login/', views.user_login , name='login'),
    path('profile/', views.user_profile , name='profile'),
    path('logout/', views.user_logout , name='logout'),
    path('teacher/', views.user_teacher , name='teacher'),
    path('student/', views.user_student , name='student'),
]

