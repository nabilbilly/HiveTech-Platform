from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.Login, name='Login'),
]