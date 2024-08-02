from django.urls import path
from . import views

urlpatterns = [
    path('', views.Talentpage, name='Talent-page'),
    path('DevCommunity/', views.DevCommunityView, name='DevCommunity-page'),
    path('DonatePage/', views.DonatePage, name='Donate-Page'),
    path('about.html/', views.Aboutuspage, name='About_us-page'),
    path('job/', views.job_view, name='Job/jobpage'),
]
