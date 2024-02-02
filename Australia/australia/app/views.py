from django.shortcuts import render
from .models import *

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from . models import *
# Create your views here.



def error_404(request, exception):
    return render(request, 'app/error.html')
# Create your views here.
def index(request):
    
    return render(request,'app/index.html')



def services(request):
    datails= Service.objects.all()
    p=Paginator(datails,4)
    page_number= request.GET.get('page')
    datails=p.get_page(page_number)
    return render(request,'app/services.html',{'service':datails})

def serviceDetail(request,slug):
    datails= Service.objects.all()
    details= Service.objects.get(service_slug=slug)
    return render(request,'app/serviceDetail.html',{'details':details,'service':datails})

def program(request):
    datails= Programs.objects.all()
    p=Paginator(datails,4)
    page_number= request.GET.get('page')
    datails=p.get_page(page_number)
    return render(request,'app/program.html',{'program':datails})

def program_detail(request,slug):
    datails= Programs.objects.all()
    details= Programs.objects.get(program_slug=slug)
    return render(request,'app/programDetail.html',{'details':details,'program':datails})

def about(request):
    about=Company_Info.objects.all()
    testimonial=Testimonial.objects.all()
    return render(request,'app/about.html',{'about':about[0:1],'testimonail':testimonial})


def event(request):
    about=Event.objects.all()
    p=Paginator(about,4)
    page_number= request.GET.get('page')
    about=p.get_page(page_number)
    return render(request,'app/events.html',{'event':about})


def eventDetail(request,slug):
    datails= Event.objects.all()
    details= Event.objects.get(event_slug=slug)
    return render(request,'app/eventDetail.html',{'details':details,'event':datails})

def team(request,slug):
    about=Team.objects.all()
    org_cat= OrganizationChart.objects.get(org_slug=slug)
    team=Team.objects.filter(organizationChart=org_cat)
    p=Paginator(team,6)
    page_number= request.GET.get('page')
    team=p.get_page(page_number)
    return render(request,'app/team.html',{'team1':about,'team':team})



def careers(request):
    datails= Careers.objects.all()
    p=Paginator(datails,6)
    page_number= request.GET.get('page')
    datails=p.get_page(page_number)
    # details= Careers.objects.get(career_slug=slug)
    return render(request,'app/careers.html',{'career':datails})


def contact(request):
    # details= contact.objects.get(career_slug=slug)
    return render(request,'app/contact.html')


