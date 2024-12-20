# dashboard/forms.py
from django import forms 
from ckeditor.widgets import CKEditorWidget
from about.models import About
from gallery.models import Gallery
from products.models import Category, Product
from .models import MediaMention, CustomerReview
from home.models import CarouselSlide
from about.models import Service, TeamMember


class MediaMentionForm(forms.ModelForm):
    class Meta:
        model = MediaMention
        fields = ['title', 'source', 'url', 'publish_date', 'description', 
                 'image', 'is_active', 'order']
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'meta_title', 
                 'meta_description', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'price', 
                 'stock', 'image', 'meta_title', 'meta_description', 
                 'is_featured', 'is_active']
        widgets = {
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'short_description', 'mission', 'vision', 
                 'story', 'image', 'years_experience', 'completed_jobs', 
                 'happy_customers', 'meta_title', 'meta_description']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 4}),
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }



class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'bio', 'image', 'order', 'is_active']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'media_type', 'image', 
                 'video', 'video_url', 'is_featured', 'is_active', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'video_url': forms.URLInput(attrs={'placeholder': 'YouTube veya Vimeo URL'})
        }

class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ['name', 'review', 'rating', 'is_approved']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class CarouselSlideForm(forms.ModelForm):
    class Meta:
        model = CarouselSlide
        fields = ['title', 'description', 'image', 'button_text', 
                 'button_url', 'order', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }