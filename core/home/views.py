# home/views.py
from django.shortcuts import render
from .models import CarouselSlide
from about.models import About
from products.models import Product
from gallery.models import Gallery
from dashboard.models import MediaMention  # MediaMention modelini dashboard'dan import ediyoruz
from reviews.models import Review


def home(request):
    context = {
        'carousel_slides': CarouselSlide.objects.filter(is_active=True).order_by('order')[:5],
        'about': About.objects.first(),  
        'latest_images': Gallery.objects.filter(is_active=True, media_type='image').order_by('-created_at')[:10],
        'featured_products': Product.objects.filter(is_active=True, is_featured=True).order_by('-created_at')[:10],  # available -> is_active, featured -> is_featured
        'media_mentions': MediaMention.objects.filter(is_active=True).order_by('-publish_date')[:5],  # publication_date -> publish_date
        'approved_reviews': Review.objects.filter(is_approved=True).order_by('-created_at')[:20]  # Son 5 onaylı yorum


    }
    return render(request, 'home/index.html', context)