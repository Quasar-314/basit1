# gallery/views.py
from django.shortcuts import render
from .models import Gallery  # Sadece Gallery'yi import ediyoruz

def gallery_list(request):
    gallery_items = Gallery.objects.filter(is_active=True).order_by('order', '-created_at')
    context = {
        'gallery_items': gallery_items
    }
    return render(request, 'gallery/gallery_list.html', context)