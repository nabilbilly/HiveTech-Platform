from django.shortcuts import render


# Create your views here.

def Talentpage(request):
    return render(request,'base.html')

def dev_community_view(request):
    return render(request, 'DevCommunity.html')
