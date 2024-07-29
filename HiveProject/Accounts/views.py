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
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            login(request, user)
            messages.success(request, 'Signup successful! Welcome to Hive.')
            return redirect('Login')
        else:
            # Display all form errors
            for field in form.errors:
                for error in form.errors[field]:
                    if field == 'password2' and error == 'Passwords do not match':
                        messages.error(request, "Passwords do not match")
                    elif field == 'password1' and error == 'Passwords do not match':
                         messages.error(request, "Passwords do not match")
                    else:
                        messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "Accounts/Signup.html", {'form': form})

def Login(request):
    page = 'Login'
    
    # if request.user.is_authenticated:
    #     return redirect('Login')
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, "Accounts/login.html", {'page': page})

        user = authenticate(request, email=user.email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Username or Password does not exist')
    
    context = {'page': page}
    return render(request, "Accounts/login.html", context)

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
