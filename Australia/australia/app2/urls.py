from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name ='dashboard'
urlpatterns = [
        path('',views.index,name='index'),
        path('login/', views.login, name='login'),
        path('logout', views.userlogout, name='logout'),

        path('Company_Info', views.companyinfo, name='Company_Info'),


        path('add_Service',views.add_edit_Service,name='add_Service'),
        path('edit_Service/<int:id>/',views.add_edit_Service,name='edit_Service'),
        path('deleteService/<int:id>/',views.deleteService,name='deleteService'),
        path('Service',views.service,name='Service'),
        
        path('add_Breadcrumb',views.add_edit_Breadcrumb,name='add_Breadcrumb'),
        path('edit_Breadcrumb/<int:id>/',views.add_edit_Breadcrumb,name='edit_Breadcrumb'),
        path('deleteBreadcrumb/<int:id>/',views.deleteBreadcrumb,name='deleteBreadcrumb'),
        path('Breadcrumb/',views.breadcrumb,name='Breadcrumb'),
        
        
        path('add_Program',views.add_edit_Program,name='add_Program'),
        path('edit_Program/<int:id>/',views.add_edit_Program,name='edit_Program'),
        path('deleteProgram/<int:id>/',views.deleteProgram,name='deleteProgram'),
        path('Program',views.program,name='Program'),
        
        path('add_Career',views.add_edit_Career,name='add_Career'),
        path('edit_Career/<int:id>/',views.add_edit_Career,name='edit_Career'),
        path('deleteCareer/<int:id>/',views.deleteCareer,name='deleteCareer'),
        path('Career/',views.Career,name='Career'),
        
        path('add_Testimonial',views.add_edit_Testimonial,name='add_Testimonial'),
        path('edit_Testimonial/<int:id>/',views.add_edit_Testimonial,name='edit_Testimonial'),
        path('deleteTestimonial/<int:id>/',views.deleteTestimonial,name='deleteTestimonial'),
        path('Testimonial',views.testimonial,name='Testimonial'),
        
        path('add_Event',views.add_edit_Event,name='add_Event'),
        path('edit_Event/<int:id>/',views.add_edit_Event,name='edit_Event'),
        path('deleteEvent/<int:id>/',views.deleteEvent,name='deleteEvent'),
        path('Event',views.event,name='Event'),
        
        path('add_OrganizationChart',views.add_edit_OrganizationChart,name='add_OrganizationChart'),
        path('edit_OrganizationChart/<int:id>/',views.add_edit_OrganizationChart,name='edit_OrganizationChart'),
        path('deleteOrganizationChart/<int:id>/',views.deleteOrganizationChart,name='deleteOrganizationChart'),
        path('OrganizationChart',views.organizationChart,name='OrganizationChart'),
        
        path('add_Team',views.add_edit_Team,name='add_Team'),
        path('edit_Team/<int:id>/',views.add_edit_Team,name='edit_Team'),
        path('deleteTeam/<int:id>/',views.deleteTeam,name='deleteTeam'),
        path('Team',views.team,name='Team'),
        
        path('add_RepresentInstitute',views.add_edit_RepresentInstitute,name='add_RepresentInstitute'),
        path('edit_RepresentInstitute/<int:id>/',views.add_edit_RepresentInstitute,name='edit_RepresentInstitute'),
        path('deleteRepresentInstitute/<int:id>/',views.deleteRepresentInstitute,name='deleteRepresentInstitute'),
        path('RepresentInstitute/',views.representInstitute,name='RepresentInstitute'),
        
        
        path('add_SliderImg',views.add_edit_SliderImg,name='add_SliderImg'),
        path('edit_SliderImg/<int:id>/',views.add_edit_SliderImg,name='edit_SliderImg'),
        path('deleteSliderImg/<int:id>/',views.deleteSliderImg,name='deleteSliderImg'),
        path('SliderImg/',views.sliderImg,name='SliderImg'),
        
        
        path('change_password/', views.change_password, name='change_password'),
        


]+ static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)