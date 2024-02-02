from django import forms
from app.models import *
from ckeditor.fields import RichTextField
# from ckeditor.widgets import CKEditorWidget
# from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'



        

class ProgramsForm(forms.ModelForm):
    class Meta:
        model = Programs
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class OrganizationChartForm(forms.ModelForm):
    class Meta:
        model = OrganizationChart
        fields = '__all__'



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class RepresentInstituteForm(forms.ModelForm):
    class Meta:
        model = RepresentInstitute
        fields = '__all__'


class Company_InfoForm(forms.ModelForm):
    class Meta:
        model = Company_Info
        fields = '__all__'
        
        
class BreadcrumbForm(forms.ModelForm):
    class Meta:
        model = Breadcrumb
        fields = '__all__'


class SliderImgForm(forms.ModelForm):
    class Meta:
        model = SliderImg
        fields = '__all__'
# # forms.py
# from django.forms import inlineformset_factory


# class ProductCategoryItemsForm(forms.ModelForm):
#     class Meta:
#         model = ProductCategoryItems
#         fields = ['name', 'sub_category', 'description', 'order_number']

# ProductImageFormSet = inlineformset_factory(
#     ProductCategoryItems,
#     ProductImage,
#     fields=['image'],
#     widgets={'image': forms.ClearableFileInput(attrs={'required': 'required', 'class': 'form-control'})},
#     extra=1 # Set extra to 0 to start with no extra forms1
# )


# # class ProductCategoryItemsForm(forms.ModelForm):
# #     class Meta:
# #         model = ProductCategoryItems
# #         fields = '__all__'
# # class ProductImageForm(forms.ModelForm):
# #     class Meta:
# #         model = ProductImage
# #         fields = ['image']
# #     def increase_num_files(self):
# #         self.fields['image'].max_num_files += 1
# #         return self
# # ProductImageFormSet = forms.inlineformset_factory(
# #     ProductCategoryItems,
# #     ProductImage,
# #     form=ProductImageForm,
# #     fields=['image'],
# #     can_delete=True,
# #     extra=10,  # Set to 0 to prevent automatic generation of extra forms10
# # )

# # class ProductImageForm(forms.ModelForm):
# #     class Meta:
# #         model = ProductImage
# #         fields = ['image']
# #         widgets = {
# #             'image': forms.ClearableFileInput(attrs={'required': 'required', 'class': 'form-control'}),
# #         }
# class SubProductCategoryForm(forms.ModelForm):
#     class Meta:
#         model = SubProductCategory
#         fields = '__all__'

# class MainProductCategoryForm(forms.ModelForm):
#     class Meta:
#         model = MainProductCategory
#         fields = '__all__'

# class BannerImgForm(forms.ModelForm):
#     class Meta:
#         model = BannerImg
#         fields = '__all__'

# class SliderForm(forms.ModelForm):
#     class Meta:
#         model = Slider
#         fields = '__all__'

# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = ContactUs
#         fields = '__all__'
        
# class AboutUsForm(forms.ModelForm):
#     class Meta:
#         model = AboutUs
#         fields = '__all__'


# class CompanyInfoForm(forms.ModelForm):
#     class Meta:
#         model = CompanyInfo
#         fields ='__all__'
        
# # class DigitalMarketingForm(forms.ModelForm):
# #     description = forms.CharField(widget=CKEditorUploadingWidget())
# #     class Meta:
# #         model = DigitalMarketing
# #         fields ='__all__'
# #         # description = forms.CharField(widget=forms.Textarea)
