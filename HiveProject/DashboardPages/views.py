from django.shortcuts import render

# Create your views here.
def job_view(request):
    return render(request, 'Job/jobpage.html')
