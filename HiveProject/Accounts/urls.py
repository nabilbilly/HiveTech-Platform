from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.Login, name='Login'),
    path('home/', views.Home, name='home'),
    path('ForgotPasswordEmail/', views.ForgotPasswordEmail, name='ForgotPasswordEmail'),
    path('VerificationCode/', views.VerifyOTP, name='VerificationCode'),
    path('PasswordReset/', views.PasswordReset, name='PasswordReset'),
    path('reset/<uidb64>/<token>/', views.PasswordReset, name='password_reset'),
]
