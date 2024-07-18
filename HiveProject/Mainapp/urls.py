from django.urls import path
from . import views

urlpatterns = [
    path('', views.Talentpage, name='Talent-page'),
    path('DevCommunity/', views.DevCommunityView, name='DevCommunity-Page'),
]
