from django.urls import path
from . import views

urlpatterns = [
    path('', views.Talentpage, name='Talent-page'),
    path('DevCommunity/', views.DevCommunityView, name='DevCommunity-page'),
    path('DonatePage/', views.DonatePage, name='Donate-Page'),
    path('AboutUs/', views.AboutUsPage, name='About_us-page'),
]
