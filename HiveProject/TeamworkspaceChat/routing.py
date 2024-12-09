from django.urls import path , include
from .consumers import ChatConsumer
from . import consumers

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    # path("" , ChatConsumer.as_asgi()) , 
    path("ws/team/<slug:team_slug>/", ChatConsumer.as_asgi())
] 
