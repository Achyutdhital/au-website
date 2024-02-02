from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from django.views import View
from account.models import User
from django.contrib.auth import authenticate, login, logout
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth
from . forms import *
from app.models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from . new_file_handler import validate_file
from django.http import JsonResponse


def login(request):
    try:
        if request.user.is_authenticated:
            return render(request,'app2/index.html')
        if request.method =="POST":
            email = request.POST['useremail']
            print(email)
            password = request.POST['password']
            print(password)
            # user_obj = User.objects.filter(email=email)
            user_obj = authenticate(email=email, password=password)
            print(user_obj)
            if not user_obj: #not user_obj.exists():
                messages.warning(request,"Invalid username and password...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj = authenticate(email=email, password=password)
            if user_obj and user_obj.is_superuser or user_obj.is_editor:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            messages.warning(request,'Inavlid Password')
            return redirect('dashboard:login')
        return render(request,'app2/login.html')
    except Exception as e:
        print(e)
        messages.warning(request,'something wrong...')
        return redirect('dashboard:login')

@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('dashboard:login')


@login_required
def index(request):
    return render(request,'app2/index.html')


@login_required
def companyinfo(request):
    instance = None
    try:
        if id:
            instance = Company_Info.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Company_Info.')
        return redirect('dashboard:Company_Info')

    if request.method == 'POST':
        form = Company_InfoForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Company_Info edited successfully.')
                return redirect('dashboard:Company_Info')  # Redirect to the edited Company_Info's details page
            else:  # Add operation
                messages.success(request, 'Company_Info added successfully.')
                return redirect('dashboard:Company_Info')  # Redirect to the page for adding new Company_Infos
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = Company_InfoForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Company_Info.html', context)



@login_required
def add_edit_SliderImg(request, id=None):
    instance = None
    try:
        if id:
            instance = SliderImg.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the SliderImg Image.')
        return redirect('dashboard:add_SliderImg')

    if request.method == 'POST':
        form = SliderImgForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'SliderImg Image edited successfully.')
                return redirect('dashboard:edit_SliderImg', id=instance.id)  # Redirect to the edited slider Image's details page
            else:  # Add operation
                messages.success(request, 'slider Image added successfully.')
                return redirect('dashboard:add_SliderImg')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = SliderImgForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_SliderImg.html', context)

@login_required
def sliderImg(request):
    sliderImg=SliderImg.objects.all()
    p=Paginator(sliderImg,10)
    page_number= request.GET.get('page')
    sliderImg=p.get_page(page_number)
    return render(request, 'app2/sliderImg.html',{'details':sliderImg})

@login_required
def deleteSliderImg(request, id):
    record = get_object_or_404(SliderImg, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:SliderImg')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/SliderImg.html', {'details': record})




@login_required
def add_edit_RepresentInstitute(request, id=None):
    instance = None
    try:
        if id:
            instance = RepresentInstitute.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the RepresentInstitute .')
        return redirect('dashboard:add_RepresentInstitute')

    if request.method == 'POST':
        form = RepresentInstituteForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'RepresentInstitute  edited successfully.')
                return redirect('dashboard:edit_RepresentInstitute', id=instance.id)  # Redirect to the edited slider Image's details page
            else:  # Add operation
                messages.success(request, 'RepresentInstitute added successfully.')
                return redirect('dashboard:add_RepresentInstitute')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = RepresentInstituteForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_RepresentInstitute.html', context)

@login_required
def representInstitute(request):
    representInstitute=RepresentInstitute.objects.all()
    p=Paginator(representInstitute,10)
    page_number= request.GET.get('page')
    representInstitute=p.get_page(page_number)
    return render(request, 'app2/RepresentInstitute.html',{'details':representInstitute})

@login_required
def deleteRepresentInstitute(request, id):
    record = get_object_or_404(RepresentInstitute, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:RepresentInstitute')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/RepresentInstitute.html', {'details': record})




@login_required
def add_edit_Team(request, id=None):
    instance = None
    try:
        if id:
            instance = Team.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Team .')
        return redirect('dashboard:add_Team')

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Team  edited successfully.')
                return redirect('dashboard:edit_Team', id=instance.id)  # Redirect to the edited slider 's details page
            else:  # Add operation
                messages.success(request, 'Team  added successfully.')
                return redirect('dashboard:add_Team')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = TeamForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Team.html', context)


@login_required
def team(request):
    team=Team.objects.all()
    p=Paginator(team,10)
    page_number= request.GET.get('page')
    team=p.get_page(page_number)
    return render(request, 'app2/team.html',{'details':team})


@login_required
def deleteTeam(request, id):
    record = get_object_or_404(Team, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Team')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Team.html', {'details': record})
    
    
    


@login_required
def add_edit_OrganizationChart(request, id=None):
    instance = None
    try:
        if id:
            instance = OrganizationChart.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the OrganizationChart .')
        return redirect('dashboard:add_OrganizationChart')

    if request.method == 'POST':
        form = OrganizationChartForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'OrganizationChart  edited successfully.')
                return redirect('dashboard:edit_OrganizationChart', id=instance.id)  # Redirect to the edited slider Image's details page
            else:  # Add operation
                messages.success(request, 'Organization chart added successfully.')
                return redirect('dashboard:add_OrganizationChart')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = OrganizationChartForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_OrganizationChart.html', context)

@login_required
def organizationChart(request):
    organizationChart=OrganizationChart.objects.all()
    p=Paginator(organizationChart,10)
    page_number= request.GET.get('page')
    organizationChart=p.get_page(page_number)
    return render(request, 'app2/OrganizationChart.html',{'details':organizationChart})

@login_required
def deleteOrganizationChart(request, id):
    record = get_object_or_404(OrganizationChart, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:OrganizationChart')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/OrganizationChart.html', {'details': record})



@login_required
def add_edit_Event(request, id=None):
    instance = None
    try:
        if id:
            instance = Event.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Event .')
        return redirect('dashboard:add_Event')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Event  edited successfully.')
                return redirect('dashboard:edit_Event', id=instance.id)  # Redirect to the edited slider 's details page
            else:  # Add operation
                messages.success(request, 'Event  added successfully.')
                return redirect('dashboard:add_Event')  # Redirect to the page for adding new slider s
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = EventForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Event.html', context)

@login_required
def event(request):
    event=Event.objects.all()
    p=Paginator(event,10)
    page_number= request.GET.get('page')
    event=p.get_page(page_number)
    return render(request, 'app2/Event.html',{'details':event})

@login_required
def deleteEvent(request, id):
    record = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Event')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Event.html', {'details': record})







@login_required
def add_edit_Program(request, id=None):
    instance = None
    try:
        if id:
            instance = Programs.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Program .')
        return redirect('dashboard:add_Program')

    if request.method == 'POST':
        form = ProgramsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Program  edited successfully.')
                return redirect('dashboard:edit_Program', id=instance.id)  # Redirect to the edited slider Image's details page
            else:  # Add operation
                messages.success(request, 'program added successfully.')
                return redirect('dashboard:add_Program')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ProgramsForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Program.html', context)

@login_required
def program(request):
    program=Programs.objects.all()
    p=Paginator(program,10)
    page_number= request.GET.get('page')
    program=p.get_page(page_number)
    return render(request, 'app2/Program.html',{'details':program})

@login_required
def deleteProgram(request, id):
    record = get_object_or_404(Programs, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Program')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Program.html', {'details': record})
    

@login_required
def add_edit_Testimonial(request, id=None):
    instance = None
    try:
        if id:
            instance = Testimonial.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Testimonial .')
        return redirect('dashboard:add_Testimonial')

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Testimonial  edited successfully.')
                return redirect('dashboard:edit_Testimonial', id=instance.id)  # Redirect to the edited slider 's details page
            else:  # Add operation
                messages.success(request, 'Testimonial  added successfully.')
                return redirect('dashboard:add_Testimonial')  # Redirect to the page for adding new slider s
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = TestimonialForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Testimonial.html', context)

@login_required
def testimonial(request):
    testimonial=Testimonial.objects.all()
    p=Paginator(testimonial,10)
    page_number= request.GET.get('page')
    testimonial=p.get_page(page_number)
    return render(request, 'app2/testimonial.html',{'details':testimonial})

@login_required
def deleteTestimonial(request, id):
    record = get_object_or_404(Testimonial, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Testimonial')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Testimonial.html', {'details': record})
  
  
  
@login_required
def add_edit_Career(request, id=None):
    instance = None
    try:
        if id:
            instance = Careers.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Career .')
        return redirect('dashboard:add_Career')

    if request.method == 'POST':
        form = CareersForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Career  edited successfully.')
                return redirect('dashboard:edit_Career', id=instance.id)  # Redirect to the edited slider 's details page
            else:  # Add operation
                messages.success(request, 'Career  added successfully.')
                return redirect('dashboard:add_Career')  # Redirect to the page for adding new slider s
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = CareersForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Career.html', context)

@login_required
def Career(request):
    Career=Careers.objects.all()
    p=Paginator(Career,10)
    page_number= request.GET.get('page')
    Career=p.get_page(page_number)
    return render(request, 'app2/Career.html',{'details':Career})

@login_required
def deleteCareer(request, id):
    record = get_object_or_404(Careers, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Career')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Career.html', {'details': record})  





@login_required
def add_edit_Service(request, id=None):
    instance = None
    try:
        if id:
            instance = Service.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Service .')
        return redirect('dashboard:add_Service')

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Service  edited successfully.')
                return redirect('dashboard:edit_Service', id=instance.id)  # Redirect to the edited slider 's details page
            else:  # Add operation
                messages.success(request, 'Service  added successfully.')
                return redirect('dashboard:add_Service')  # Redirect to the page for adding new slider s
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ServiceForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Service.html', context)

@login_required
def service(request):
    service=Service.objects.all()
    p=Paginator(service,10)
    page_number= request.GET.get('page')
    service=p.get_page(page_number)
    return render(request, 'app2/Service.html',{'details':service})

@login_required
def deleteService(request, id):
    record = get_object_or_404(Service, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Service')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Service.html', {'details': record})
    
    
    
@login_required
def add_edit_Breadcrumb(request, id=None):
    instance = None
    try:
        if id:
            instance = Breadcrumb.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Breadcrumb Image.')
        return redirect('dashboard:add_Breadcrumb')

    if request.method == 'POST':
        form = BreadcrumbForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Breadcrumb Image edited successfully.')
                return redirect('dashboard:edit_Breadcrumb', id=instance.id)  # Redirect to the edited slider Image's details page
            else:  # Add operation
                messages.success(request, 'Breadcrumb Image added successfully.')
                return redirect('dashboard:add_Breadcrumb')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = BreadcrumbForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Breadcrumb.html', context)

@login_required
def breadcrumb(request):
    breadcrumbs=Breadcrumb.objects.all()
    p=Paginator(breadcrumbs,10)
    page_number= request.GET.get('page')
    breadcrumbs=p.get_page(page_number)
    return render(request, 'app2/Breadcrumb.html',{'details':breadcrumbs})

@login_required
def deleteBreadcrumb(request, id):
    record = get_object_or_404(Breadcrumb, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Breadcrumb')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Breadcrumb.html', {'details': record})
  




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)  # Important to update the session after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard:change_password')  # Redirect to the same view after successful password change
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'app2/change_password.html', {'form': form})

