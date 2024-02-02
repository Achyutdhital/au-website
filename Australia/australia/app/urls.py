
from django.urls import path
from . import views 
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


app_name="app"

urlpatterns = [
    path('', views.index,name='index'),    
    path('services', views.services,name='services'),  
    path('event/', views.event,name='event'), 
    path('eventDetail/<slug:slug>', views.eventDetail,name='eventDetail'),
    path('careers/', views.careers,name='careers'),
    path('team/<slug:slug>', views.team,name='team'),
    path('serviceDetail/<slug:slug>', views.serviceDetail,name='serviceDetail'),
    
    
    path('program', views.program,name='program'),  
    path('programDetail/<slug:slug>', views.program_detail,name='programDetail'),
    path('about/', views.about,name='about'), 
    path('contact/', views.contact,name='contact'), 
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),


]+ static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


