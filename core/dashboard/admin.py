# dashboard/admin.py
from django.contrib import admin
from .models import CustomerReview, MediaMention

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at', 'is_approved')
    list_filter = ('rating', 'is_approved', 'created_at')
    search_fields = ('name', 'review')
    list_editable = ('is_approved',)
    
    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Seçili yorumları onayla"
    
    actions = ['approve_reviews']

@admin.register(MediaMention)
class MediaMentionAdmin(admin.ModelAdmin):
    list_display = ('source', 'title', 'publish_date')
    list_filter = ('publish_date', 'source')
    search_fields = ('title', 'source', 'description')

