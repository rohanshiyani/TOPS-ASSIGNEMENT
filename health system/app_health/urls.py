"""
URL configuration for pro_health project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from app_health import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('otp/', views.otp, name='otp'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('forgot_otp/', views.forgot_otp, name='forgot_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('doctor/', views.doctor, name='doctor'),
    path('disease/', views.disease, name='disease'),
    path('medicine/', views.medicine, name='medicine'),
    path('doctor_single/<int:pk>', views.doctor_single, name='doctor_single'),
    path('disease_single/<int:pk>', views.disease_single, name='disease_single'),
    path('medicine_single/<int:pk>', views.medicine_single, name='medicine_single'),
    
    

]
