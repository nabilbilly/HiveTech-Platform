from django.urls import path
from . import views

urlpatterns = [
    path('', views.Talentpage, name='Talent-page'),
    path('DevCommunity.html', views.dev_community_view, name='DevCommunity-page'),
]
