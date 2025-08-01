# home/admin.py
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.db.models import Count
from django.core.exceptions import ValidationError

from products.models import Product, Category
from gallery.models import Gallery
from contact.models import Contact
from dashboard.models import CustomerReview, MediaMention  # Değiştirildi - artık dashboard'dan import ediyoruz
from .models import CarouselSlide

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('order',)

    def save_model(self, request, obj, form, change):
        try:
            obj.clean()
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            messages.error(request, e.message)


class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        return app_list

    def index(self, request, extra_context=None):
        # İstatistikleri topla
        stats = {
            'total_products': Product.objects.count(),
            'total_categories': Category.objects.count(),
            'total_gallery_items': Gallery.objects.count(),
            'unread_messages': Contact.objects.filter(is_read=False).count(),
            'pending_reviews': CustomerReview.objects.filter(approved=False).count(),
            'media_mentions': MediaMention.objects.count(),
        }
        
        # Son eklenen ürünler
        latest_products = Product.objects.order_by('-created_at')[:5]
        
        # Son mesajlar
        latest_contacts = Contact.objects.filter(is_read=False).order_by('-created_at')[:5]
        
        # Kategori bazlı ürün sayıları
        categories_with_counts = Category.objects.annotate(
            product_count=Count('product')
        ).order_by('-product_count')[:5]

        context = {
            **self.each_context(request),
            'title': 'Dashboard',
            'stats': stats,
            'latest_products': latest_products,
            'latest_contacts': latest_contacts,
            'categories_with_counts': categories_with_counts,
        }
        if extra_context:
            context.update(extra_context)
            
        return TemplateResponse(request, 'admin/dashboard.html', context)

# Admin sitesini özelleştir
admin_site = CustomAdminSite(name='custom_admin')

# Modelleri yeni admin sitesine kaydet
admin_site.register(Product)
admin_site.register(Category)
admin_site.register(Gallery)
admin_site.register(Contact)