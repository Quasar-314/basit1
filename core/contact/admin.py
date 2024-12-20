# contact/admin.py
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'ip_address', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message', 'ip_address']
    readonly_fields = ['created_at', 'ip_address']
    list_editable = ['is_read']
# reviews/admin.py
