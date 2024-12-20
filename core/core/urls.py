# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, ProductSitemap, GallerySitemap
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'gallery': GallerySitemap,
}


urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('home.urls')),
     path('urunler/', include('products.urls')),
     path('galeri/', include('gallery.urls')),
     path('hakkimizda/', include('about.urls')),
     path('iletisim/', include('contact.urls')),
     # SEO URLs - Tekrar eden kaldırıldı
     path('sitemap.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),
     path('robots.txt', cache_page(86400)(TemplateView.as_view(
         template_name="robots.txt", content_type="text/plain"))),
     path('dashboard/', include('dashboard.urls')),
     path('reviews/', include('reviews.urls', namespace='reviews')),
        

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)