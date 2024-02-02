from . models import *


def org_ctg(request):
    org= OrganizationChart.objects.all()
    return({
        'org':org
    })


def representInstitute(request):
    represent=RepresentInstitute.objects.all()
    return({
        'represent':represent
    })
    
def company_Info(request):
    contactinfo = Company_Info.objects.first()
    return ({
        'company_Info':contactinfo
    })

def about_us(request):
    aboutus = Company_Info.objects.first()
    return ({
        'about':aboutus
    })
    
def service(request):
    service = Service.objects.all()
    return ({
        'service':service
    })
    
    
def program(request):
    program = Programs.objects.all()
    return ({
        'program':program
    })

    
def company_info(request):
    info = Company_Info.objects.first()
    return ({
        'info':info
    })
    

def homeSlider(request):
    slider = SliderImg.objects.all()
    return ({
        'slider':slider
    })
    
def breadcrumbs(request):
    contact = Breadcrumb.objects.filter(title='contact')
    about = Breadcrumb.objects.filter(title='about')
    service = Breadcrumb.objects.filter(title='service')
    program = Breadcrumb.objects.filter(title='program')
    career = Breadcrumb.objects.filter(title='career')
    event = Breadcrumb.objects.filter(title='event')

    return ({
        'contactImg':contact,
        'aboutImg':about,
        'serviceImg':service,
        'programImg':program,
        'eventImg':event,
        'careerImg':career
    })