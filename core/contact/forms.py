# contact/forms.py
from django import forms
from core.forms import SecureForm
from .models import Contact
from django.core.exceptions import ValidationError
import re

class ContactForm(SecureForm, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            phone = re.sub(r'\D', '', phone)
            if not re.match(r'^\d{10,11}$', phone):
                raise ValidationError('Geçersiz telefon numarası')
        return phone