from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .forms import CustomUserCreationForm
import re
import random
from django.core.cache import cache


def is_password_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+]", password):
        return False
    return True


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email verified successfully. You can now log in.')
        return redirect('Login')
    else:
        messages.error(request, 'The verification link is invalid or has expired.')
        return redirect('SignUp')


def send_verification_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = request.build_absolute_uri(reverse('verify_email', kwargs={'uidb64': uid, 'token': token}))

    subject = 'Verify your email'
    message = render_to_string('Accounts/VerificationEmail.html', {
        'user': user,
        'verification_link': verification_link,
    })
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email, fail_silently=False, html_message=message)


def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, 'Invalid email address.')
                return render(request, "Accounts/Signup.html", {'form': form})

            if not is_password_strong(password):
                messages.error(request, 'Password is too weak. It must be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters.')
                return render(request, "Accounts/Signup.html", {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, "Accounts/Signup.html", {'form': form})

            user = form.save(commit=False)
            user.username = user.email
            user.is_active = False
            user.save()

            try:
                send_verification_email(user, request)
                messages.success(request, 'Please check your email to verify your account.')
                return redirect('Login')
            except Exception as e:
                user.delete()  # Roll back user creation if email sending fails
                messages.error(request, f'Failed to send verification email. Please try again later. Error: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request, "Accounts/Signup.html", {'form': form})


def Login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, "Accounts/login.html")

        if not user.is_active:
            messages.error(request, 'Please verify your email before logging in.')
            return render(request, "Accounts/login.html")

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Talent-page')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, "Accounts/login.html")


@login_required
def Home(request):
    return render(request, "Accounts/home.html")


@login_required
def LogoutUser(request):
    logout(request)
    return redirect('home')

def generate_otp():
    return str(random.randint(100000, 999999))



def send_otp_email(user, otp):
    subject = 'Password Reset OTP'
    context = {
        'user': user,
        'otp': otp,
    }
    message = render_to_string('Accounts/password_reset_otp.html', context)
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
        html_message=message
    )

def ForgotPasswordEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = generate_otp()
            cache_key = f"password_reset_otp_{user.id}"
            cache.set(cache_key, otp, timeout=600)  # 600 seconds = 10 minutes

            send_otp_email(user, otp)
            messages.success(request, 'An OTP has been sent to your email. Please check your inbox.')

            return redirect('verify-otp', user_id=user.id)
        except User.DoesNotExist:
            messages.error(request, 'No user with that email address exists.')
        return redirect('Login')
    return render(request, "Accounts/ForgotPasswordEmail.html")


def VerifyOTP(request, user_id):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        cache_key = f"password_reset_otp_{user_id}"
        stored_otp = cache.get(cache_key)

        if stored_otp and entered_otp == stored_otp:
            cache.delete(cache_key)
            return redirect('reset_password', user_id=user_id)
        else:
            messages.error(request, 'Invalid or expired OTP. Please try again.')

    return render(request, "Accounts/VerifyOTP.html", {'user_id': user_id})



def PasswordReset(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            if is_password_strong(new_password):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been reset successfully. You can now log in with your new password.')
                return redirect('Login')
            else:
                messages.error(request, 'Password is too weak. It must be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters.')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, "Accounts/PasswordReset.html", {'user': user})
