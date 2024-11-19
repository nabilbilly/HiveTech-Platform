from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.Teamview, name='Teamview-Page'),
    path('Chat/', views.TeamworkspaceChat, name='Team-Workspace-Chat'),
]