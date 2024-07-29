from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.db.models import Q
from .forms import CustomUserCreationForm

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = form.save(commit=False)
                user.username = user.email
                user.is_active = False  # Deactivate account until email is confirmed
                user.save()
                return redirect('Login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "Accounts/Signup.html", {'form': form})

def Login(request):
    page = 'Login'
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, "Accounts/login.html", {'page': page})

        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, "Accounts/login.html", {'page': page})

def Home(request):
    return render(request, "Accounts/home.html")

def LogoutUser(request):
    logout(request)
    return redirect('home')

def ForgotPasswordEmail(request):
    return render(request, "Accounts/ForgotPasswordEmail.html")

def VerificationCode(request):
    return render(request, "Accounts/VerificationCode.html")

def PasswordReset(request):
    return render(request, "Accounts/PasswordReset.html")
