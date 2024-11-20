from django.shortcuts import render, redirect, get_object_or_404
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
from .models import Team, TeamMembership
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse


# @login_required(login_url='Login')
# def Teamview(request):
#     return render(request, 'Job/TeamworkspaceDashboard.html')

@login_required(login_url='Login')
def TeamworkspaceChat(request):
    return render(request, 'Job/TeamworkspaceChat.html')


@login_required
def Team_workspace_dashboard(request):
    """
    Display the dashboard for the user's teams and workspaces.
    """
    # Teams created by the user
    created_teams = Team.objects.filter(created_by=request.user)
    
    # Teams the user is a member of
    member_teams = Team.objects.filter(members__user=request.user)
    
    # Combine both queries (avoiding duplicates)
    all_teams = created_teams.union(member_teams)

    # context = {
    #     'teams': all_teams,  # Pass all teams to the template
    # }
    # Prepare a dictionary to store user roles for each team
    user_roles = {} 
    for team in all_teams: 
       membership = TeamMembership.objects.filter(team=team, user=request.user).first() 
       user_roles[team.slug] = membership.role if membership else None

    context = {
        'teams': all_teams,  # Pass all teams to the template
        'user_roles': user_roles,  # Pass user roles for conditional display
    }
    
    return render(request, 'Teamworkspace/TeamworkspaceDashboard.html', context)


@login_required
def add_team(request):
    """
    Handle creating a new team.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')

        # Check if a team with the same name already exists
        if Team.objects.filter(name=name).exists():
            messages.error(request, 'A team with this name already exists.')
            return redirect('Team-workspace-dashboard')
        
        # Create the new team and automatically set the creator as admin 
        team = Team.objects.create(name=name, description=description, created_by=request.user)
        TeamMembership.objects.create(team=team, user=request.user, role='admin')
        messages.success(request, 'Team created successfully!')
        return redirect('Team-workspace-dashboard')

    messages.error(request, 'Invalid request method.')
    return redirect('Team-workspace-dashboard')