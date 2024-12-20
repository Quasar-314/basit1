from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adınız Soyadınız'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '5',
                'placeholder': 'Puanınız (1-5 arası)'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'placeholder': 'Yorumunuz'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }