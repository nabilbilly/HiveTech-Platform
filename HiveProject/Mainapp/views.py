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




