from django.shortcuts import render


# Create your views here.

def Talentpage(request):
    return render(request,'TalentPage.html')

def DevCommunityView(request):
    return render(request, 'DevCommunity.html')

def DonatePage(request):
    return render(request, 'Donate/donatepage.html')

def Aboutuspage(request):
    return render(request, 'about.html')

def Employerspage(request):
    return render(request, 'employers.html')

def job_view(request):
    return render(request, 'Job/jobpage.html')

