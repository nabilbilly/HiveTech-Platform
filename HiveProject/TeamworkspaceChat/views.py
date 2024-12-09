from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Message

# # Create your views here.
# def chatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login-user")
#     # Retrieve the last 50 messages and reverse the queryset
#     messages = Message.objects.order_by('timestamp')[:50]
#     context = {"messages": messages}
#     return render(request, "Teamworkspace/chatPage.html", context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Teamworkspace.models import Team, TeamMembership

@login_required
def chatPage(request, team_slug):
    team = get_object_or_404(Team, slug=team_slug)
    if not TeamMembership.objects.filter(team=team, user=request.user).exists():
        return redirect("login-user")
    messages = team.messages.order_by('timestamp')[:50]
    context = {"team": team, "messages": messages}
    return render(request, "Teamworkspace/TeamworkspaceChat.html", context)
