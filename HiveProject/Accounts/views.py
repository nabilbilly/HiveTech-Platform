from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *

# Create your views here.

def SignUp(request):
    return render(request, "Accounts/Signup.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Extract email from POST data
        password = request.POST.get('password')  # Extract password from POST data

        user = auth.authenticate(request, email=email, password=password)  # Authenticate using email

        if user is not None:
            auth.login(request, user)
            return redirect('homepage')  # Redirect to a named URL pattern 'homepage'
        else:
            messages.info(request, "Wrong email or password")  # Use more accurate message
            return redirect('login')  # Redirect back to login on failure

    return render(request, "Accounts/login.html")  # Render login template on GET request


def ForgotPasswordEmail(request):
    return render(request, "Accounts/ForgotPasswordEmail.html")

def VerificationCode(request):
    return render(request, "Accounts/VerificationCode.html")

def PasswordReset(request):
    return render(request, "Accounts/PasswordReset.html")

def Homepage(request):
    return render(request, "Accounts/homepage.html")



