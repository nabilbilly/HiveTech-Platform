from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.job_view, name='Job-Page'),
    path('Teamview/', views.Teamview, name='Teamview-Page'),
]