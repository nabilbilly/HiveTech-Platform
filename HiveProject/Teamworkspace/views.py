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


@login_required
def add_member(request, slug):
    team = get_object_or_404(Team, slug=slug)
    if request.method == 'POST':
        username = request.POST.get('user_identifier')
        role = request.POST.get('role')
        description = request.POST.get('description', '')

        try:
            user = User.objects.get(username=username)
            if team.can_add_member():
                TeamMembership.objects.create(user=user, team=team, role=role, description=description)
                messages.success(request, f'Member {username} added successfully!')
            else:
                messages.error(request, 'Team already has the maximum number of members.')
        except User.DoesNotExist:
            messages.error(request, f'User with username {username} does not exist.')

        return redirect('Team-workspace-dashboard')

    messages.error(request, 'Invalid request method.')
    return redirect('Team-workspace-dashboard')

@login_required
def add_members(request, slug):
    team = get_object_or_404(Team, slug=slug)
    if not team.members.filter(user=request.user, role="admin").exists():
        messages.error(request, "Only the admin can add members.")
        return redirect("view_team", slug=slug)

    if request.method == "POST":
        username_or_email = request.POST.get("user_identifier")
        role = request.POST.get("role") 
        description = request.POST.get("description", '') 
        specify_role = request.POST.get("SpecifyRole", '')
        try:
            user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect("view_team", slug=slug)

        if team.can_add_member():
            # TeamMembership.objects.create(team=team, user=user, role="member")
            TeamMembership.objects.create(team=team, user=user, role=role, description=description, SpecifyRole=specify_role)
            messages.success(request, f"{user.username} added to the team.")
        else:
            messages.error(request, "Team already has 5 members.")
    return redirect("view_team", slug=slug)

@login_required
def view_team(request, slug):
    team = get_object_or_404(Team, slug=slug)
    members = team.members.all()
    context = {"team": team, "members": members}
    return render(request, "Teamworkspace/view_team.html", context)

@login_required
def view_team_members(request, slug):
    """
    View members of a specific team.
    """
    team = get_object_or_404(Team, slug=slug)
    members = team.members.all()
    context = {"team": team, "members": members}
    return render(request, "Teamworkspace/view_team_members.html", context)
