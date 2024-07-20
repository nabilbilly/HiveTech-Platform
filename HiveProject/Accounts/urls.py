from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.Login, name='Login'),
    path('ForgotPasswordEmail/', views.ForgotPasswordEmail, name='ForgotPasswordEmail'),
    path('VerificationCode/', views.VerificationCode, name='VerificationCode'),
    path('PasswordReset/', views.PasswordReset, name='PasswordReset'),
]
