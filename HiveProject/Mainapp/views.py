from django.shortcuts import render


# Create your views here.

def Talentpage(request):
    return render(request,'General/TalentPage.html')

def DevCommunityView(request):
    return render(request, 'General/DevCommunity.html')

def DonatePage(request):
    return render(request, 'Donate/donatepage.html')

def AboutUsPage(request):
    return render(request, 'General/About.html')

def Employerspage(request):
    return render(request, 'General/employers.html')


# introduction Page 

def ExploreInterest(request):
    return render(request, 'Introduction/ExploreInterest.html')

def ExpertedEarn(request):
    return render(request, 'Introduction/ExpertedEarn.html')

def YearsOfExperience(request):
    return render(request, 'Introduction/YearsOfExperience.html')

def JobExperience(request):
    return render(request, 'Introduction/JobExperience.html')

def LevelOfEducation(request):
    return render(request, 'Introduction/LevelOfEducation.html')

def EnglishLevel(request):
    return render(request, 'Introduction/EnglishLevel.html')

def LocationOfWork(request):
    return render(request, 'Introduction/LocationOfWork.html')

def EmploymentOption(request):
    return render(request, 'Introduction/EmploymentOption.html')

def JobListType(request):
    return render(request, 'Introduction/JobListType.html')

def WorkSchedule(request):
    return render(request, 'Introduction/WorkSchedule.html')

def TeamSetup(request):
    return render(request, 'Introduction/TeamSetup.html')

def JoinCommunity(request):
    return render(request, 'Introduction/JoinCommunity.html')

def EmailNotification(request):
    return render(request, 'Introduction/EmailNotification.html')