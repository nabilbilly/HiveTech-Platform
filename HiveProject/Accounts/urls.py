from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.Login, name='Login'),
    path('home/', views.Home, name='home'),
    path('ForgotPasswordEmail/', views.ForgotPasswordEmail, name='ForgotPasswordEmail'),
    path('verify-otp/<int:user_id>/', views.VerifyOTP, name='VerifyOTP'),
    path('reset-password/<int:user_id>/', views.PasswordReset, name='reset_password'),
    path('reset/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]
