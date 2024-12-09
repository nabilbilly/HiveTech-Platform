from django.urls import path, include
from . import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path("", chat_views.chatPage, name="chat-page"),
    path("team/<slug:team_slug>/", chat_views.chatPage, name="chat-page"),
    # Custom login view
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]