from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *
# Register your models here.

    
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id', 'title', 'image', 'description', 'created_date']
admin.site.register(Service,ServiceAdmin)


class CareersAdmin(admin.ModelAdmin):
    model = Careers
    list_display = ['id', 'title', 'link']
admin.site.register(Careers,CareersAdmin)


   
class ProgramsAdmin(admin.ModelAdmin):
    model = Programs
    list_display = ['id', 'title', 'image', 'description', 'created_date']
admin.site.register(Programs,ProgramsAdmin)



   
class BreadcrumbAdmin(admin.ModelAdmin):
    model = Breadcrumb
    list_display = ['id','breadcrumb_img','title']
admin.site.register(Breadcrumb,BreadcrumbAdmin)


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['id','starttime','endtime','description','image']
admin.site.register(Event,EventAdmin)


class OrganizationChartAdmin(admin.ModelAdmin):
    model = OrganizationChart
    list_display = ['id','name','order_number']
admin.site.register(OrganizationChart,OrganizationChartAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_display = ['id','name','description','image','designation']
admin.site.register(Testimonial,TestimonialAdmin)

class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['id','organizationChart','name','team_member_photo','member_designation','facebook_link','instagram_link']
admin.site.register(Team,TeamAdmin)


class SliderImgAdmin(admin.ModelAdmin):
    model = SliderImg
    list_display = ['id','slider_img']
admin.site.register(SliderImg,SliderImgAdmin)


class RepresentInstituteAdmin(admin.ModelAdmin):
    model = RepresentInstitute
    list_display = ['id','name','logo','link']
admin.site.register(RepresentInstitute,RepresentInstituteAdmin)


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=['location','facebook_link','youtube_link','instagram_link','location_link','email','phone','description','logo']
admin.site.register(Company_Info)

