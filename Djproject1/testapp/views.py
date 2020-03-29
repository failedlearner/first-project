from django.shortcuts import render
from testapp.models import *
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'job_list' :jobs_list}
    return render(request,'testapp/hydjobs.html', context=my_dict)

def punejobs1(request):
    jobs_list=punejobs.objects.order_by('date')
    my_dict={'job_list':jobs_list}
    return render(request,'testapp/punejobs.html', context=my_dict)

def blorejobs1(request):
    jobs_list=blorejobs.objects.order_by('date')
    my_dict={'job_list':jobs_list}
    return render(request,'testapp/blorejobs.html', context=my_dict)

def chennaijobs1(request):
    jobs_list=chennaijobs.objects.order_by('date')
    my_dict={'job_list':jobs_list}
    return render(request,'testapp/chennaijobs.html', context=my_dict)
