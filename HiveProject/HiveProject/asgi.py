"""
ASGI config for HiveProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from TeamworkspaceChat import routing
django_asgi_app = get_asgi_application()

# from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HiveProject.settings')
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "http" : get_asgi_application() , 
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )    
        )
})

ASGI_APPLICATION = 'HiveProject.asgi.application'
# application = get_asgi_application()
