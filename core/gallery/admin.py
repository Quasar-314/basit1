# gallery/admin.py
from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'is_featured', 'is_active', 'order', 'created_at')
    list_filter = ('media_type', 'is_featured', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'is_featured', 'order')
    readonly_fields = ('created_at',)