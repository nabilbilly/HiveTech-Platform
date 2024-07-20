from django.shortcuts import render

# Create your views here.

def SignUp(request):
    return render(request, "Accounts/Signup.html")

def Login(request):
    return render(request, "Accounts/login.html")

def ForgotPasswordEmail(request):
    return render(request, "Accounts/ForgotPasswordEmail.html")

def VerificationCode(request):
    return render(request, "Accounts/VerificationCode.html")

def PasswordReset(request):
    return render(request, "Accounts/PasswordReset.html")



