from django.shortcuts import render
from jobsapp.models import HydJobs,BangloreJobs,PuneJobs
# Create your views here.

def homepage(request):
    return render(request, 'jobsapp/index.html')


def hydJobs(request):
    jobs_list = HydJobs.objects.all()
    mydict = {'jobs_list':jobs_list}
    return render(request, 'jobsapp/hydjobs.html', context=mydict)


def bangloreJobs(request):
    jobs_list = PuneJobs.objects.all()
    mydict = {'jobs_list':jobs_list}
    return render(request, 'jobsapp/bangloreJobs.html', context=mydict)

def puneJobs(request):
    jobs_list = PuneJobs.objects.all()
    mydict = {'jobs_list':jobs_list}
    return render(request, 'jobsapp/puneJobs.html', context=mydict)
