# about/admin.py
from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'short_description', 'image')
        }),
        ('İçerik', {
            'fields': ('mission', 'vision', 'story')
        }),
        ('İstatistikler', {
            'fields': ('years_experience', 'completed_jobs', 'happy_customers')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Tarihler', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def has_add_permission(self, request):
        # Sadece bir kayıt olabilir
        if About.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Silme işlemini engelle
        return False