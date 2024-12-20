from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product
from gallery.models import Gallery

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:home', 'contact:contact']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated_at

class GallerySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Gallery.objects.all()

    def lastmod(self, obj):
        return obj.created_at