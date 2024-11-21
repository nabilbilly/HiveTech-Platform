from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.Team_workspace_dashboard, name='Team-workspace-dashboard'),  # Dashboard
    path('Chat/', views.TeamworkspaceChat, name='Team-Workspace-Chat'),
    path('create_team/ ', views.add_team, name='add_team'),  # Add new team
    # path('Dashboard/', views.Teamview, name='Teamview-Page'),
   
    path('add_member/<int:team_id>/', views.add_member, name='add_member'), 
    path('add_member/<slug:slug>/', views.add_members, name='add_members'), 
    path('view_team/<slug:slug>/', views.view_team, name='view_team'),
     path('view_team_members/<slug:slug>/', views.view_team_members, name='view_team_members'),
]