from django.db import models

# Create your models here.
from django.db import models
from autoslug.fields import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.

    
class Service(models.Model):
    title=models.CharField(max_length=1000)
    description=RichTextField()
    image= models.ImageField(upload_to='serviceimg',blank=True, null=True)
    created_date= models.DateField(auto_now=True)
    service_slug= AutoSlugField(populate_from='title',unique=True,blank=True)
    
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.title
        
        
class Careers(models.Model):
    title=models.CharField(max_length=1000)
    link=models.URLField(max_length=1000)
    career_slug= AutoSlugField(populate_from='title',unique=True,blank=True)

        
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=500)
    description=models.TextField()
    designation=models.CharField(max_length=500)
    image=models.ImageField(upload_to='testimonial/')
    
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.name
        
class Programs(models.Model):
    title=models.CharField(max_length=1000)
    description=RichTextField()
    image= models.ImageField(upload_to='programimg',blank=True, null=True)
    created_date= models.DateField(auto_now=True)
    program_slug= AutoSlugField(populate_from='description',unique=True,blank=True)
    
  
    
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.title
    


class Event(models.Model):
    starttime=models.TimeField()
    endtime=models.TimeField()
    startdate=models.DateField()
    enddate=models.DateField()
    eventname=models.CharField(max_length=500)
    description=RichTextField()
    location=models.CharField(max_length=500)
    image=models.ImageField(upload_to='eventimg/')
    event_slug= AutoSlugField(populate_from='eventname',unique=True,blank=True)

    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.eventname

    
class OrganizationChart(models.Model):
    name = models.CharField(max_length=200)
    org_slug= AutoSlugField(populate_from='name',unique=True,blank=True)
    order_number= models.IntegerField()
    
    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.name
    
class Team(models.Model):
    organizationChart=models.ForeignKey(OrganizationChart, on_delete=models.CASCADE, related_name='organizationChart')
    name = models.CharField(max_length=200)
    team_member_photo= models.ImageField(upload_to="team")
    member_designation= models.CharField(max_length=100)
    facebook_link= models.URLField(blank=True, null=True)
    instagram_link=models.URLField(blank=True, null=True)
    team_slug= AutoSlugField(populate_from='name',unique=True,blank=True)

    class Meta:
        ordering=['-id']
        
    def __str__(self):
        return self.name
    
 
class RepresentInstitute(models.Model):
    name = models.CharField(max_length=500)
    logo=models.ImageField(upload_to='reperesntinstitute/')
    link=models.URLField()
    
     
class Company_Info(models.Model):
    location=models.CharField(max_length=100)
    facebook_link= models.URLField(blank=True, null=True)
    youtube_link= models.URLField(blank=True, null=True,max_length=1000)
    instagram_link=models.URLField(blank=True, null=True)
    location_link=models.URLField(blank=True, null=True,max_length=1000)
    email=models.EmailField()
    logo=models.ImageField(upload_to='logo')
    phone=models.PositiveBigIntegerField()
    description=RichTextField()
    intStudent=models.PositiveIntegerField()
    scholarshipApproved=models.PositiveIntegerField()
    studentEnrolled=models.PositiveIntegerField()
    representInstitute=models.PositiveIntegerField()
    

title =(
    ('about','About'),
    ('contact','Contact'),
    ('service','Service'),
    ('program','Program'),
    ('career','Career'),
    ('event','Event')
) 

class Breadcrumb(models.Model):
    breadcrumb_img=models.FileField(upload_to='images/')
    title = models.CharField(choices=title, max_length=200)

    class Meta:
        ordering=['-id']



class SliderImg(models.Model):
    slider_img=models.FileField(upload_to='sliderimages/')
    title=models.CharField(max_length=1000)
    class Meta:
        ordering=['-id']
