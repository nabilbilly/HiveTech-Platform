from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
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
import re
import random
from django.core.cache import cache


@login_required(login_url='Login')
def Teamview(request):
    return render(request, 'Job/TeamworkspaceDashboard.html')

@login_required(login_url='Login')
def TeamworkspaceChat(request):
    return render(request, 'Job/TeamworkspaceChat.html')