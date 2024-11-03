from django.urls import path
from . import views

urlpatterns = [
    path('', views.Talentpage, name='Talent-page'),
    path('DevCommunity/', views.DevCommunityView, name='DevCommunity-page'),
    path('DonatePage/', views.DonatePage, name='Donate-Page'),
    path('AboutUs/', views.AboutUsPage, name='About_us-page'),
    path('employers/', views.Employerspage, name='Employers-Page'),
    path('ExploreInterest/', views.ExploreInterest, name='Explore-Interest'),
    path('ExpertedEarn/', views.ExpertedEarn, name='Experted-Earn'),
    path('YearsOfExperience/', views.YearsOfExperience, name='Years-Of-Experience'),
    path('JobExperience/', views.JobExperience, name='Job-Experience'),
    path('LevelOfEducation/', views.LevelOfEducation, name='Level-Of-Education'),
    path('EnglishLevel/', views.EnglishLevel, name='English-Level'),
    path('LocationOfWork/', views.LocationOfWork, name='Location-Of-Work'),
    path('EmploymentOption/', views.EmploymentOption, name='Employment-Option'),
    path('JobListType/', views.JobListType, name='Job-List-Type'),
    path('WorkSchedule/', views.WorkSchedule, name='Work-Schedule'),
    path('TeamSetup/', views.TeamSetup, name='Team-Setup'),
    path('JoinCommunity/', views.JoinCommunity, name='Join-Community'),
    path('EmailNotification/', views.EmailNotification, name='Email-Notification'),
]
