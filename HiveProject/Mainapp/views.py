from django.shortcuts import render


# Create your views here.

def Talentpage(request):
    return render(request,'base.html')

def DevCommunityView(request):
    return render(request, 'DevCommunity.html')

def DonatePage(request):
    return render(request, 'Donate/donatepage.html')
