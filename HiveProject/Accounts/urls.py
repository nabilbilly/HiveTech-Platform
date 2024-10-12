from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.Login, name='Login'), 
    path('logout/', views.LogoutUser, name='LogoutUser'),
    path('resend-verification-mail/', views.resend_verification, name='resend_verification'),
    path('ForgotPasswordEmail/', views.ForgotPasswordEmail, name='ForgotPasswordEmail'),
    path('verify-otp/<int:user_id>/', views.VerifyOTP, name='verify-otp'),
    path('PasswordReset/<int:user_id>/', views.PasswordReset, name='PasswordReset'),
    path('reset/<uidb64>/<token>/', views.verify_email, name='verify_email'),
   
]
