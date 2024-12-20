# products/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('category')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)