from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.job_view, name='Job-Page'),
]