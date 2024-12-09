from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.Team_workspace_dashboard, name='Team-workspace-dashboard'),  # Dashboard
    path('Chat/', views.TeamworkspaceChat, name='Team-Workspace-Chat'),
    path('TeamworkspaceSettings/', views.TeamworkspaceSettings, name='Team-Workspace-Settings'),
    path('create_team/ ', views.add_team, name='add_team'),  # Add new team
    # path('Dashboard/', views.Teamview, name='Teamview-Page'),
   
    path('add_member/<int:team_id>/', views.add_member, name='add_member'), 
    path('add_members/<slug:slug>/', views.add_members, name='add_members'), 
    path('view_team/<slug:slug>/', views.view_team, name='view_team'),
    path('view_team_members/<slug:slug>/', views.view_team_members, name='view_team_members'),
    path('delete_team_member/<slug:slug>/<int:user_id>/', views.delete_team_member, name='delete_team_member'),
    path('delete_team_workspace/<slug:slug>/', views.delete_team_workspace, name='delete_team_workspace'), # Delete team workspace by slug
    
    path('check_user_exists/', views.check_user_exists, name='check_user_exists'),
    path('check_team_exists/', views.check_team_exists, name='check_team_exists'),
    path('search_workspaces/', views.search_user_workspaces, name='search_workspaces'),
]