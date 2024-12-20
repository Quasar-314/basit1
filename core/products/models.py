# products/models.py
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=100)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Açıklama", blank=True)
    meta_title = models.CharField("Meta Başlık", max_length=200, blank=True)  # Yeni eklendi
    meta_description = models.TextField("Meta Açıklama", blank=True)  # Yeni eklendi
    is_active = models.BooleanField("Aktif", default=True)  # Yeni eklendi
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)  # Yeni eklendi

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    name = models.CharField("Ürün Adı", max_length=200)
    slug = models.SlugField("URL", unique=True)
    description = RichTextField("Açıklama")
    price = models.DecimalField("Fiyat", max_digits=10, decimal_places=2)  # blank ve null kaldırıldı
    image = models.ImageField("Ürün Resmi", upload_to='products/%Y/%m/')
    stock = models.PositiveIntegerField("Stok")  # blank ve null kaldırıldı
    is_active = models.BooleanField("Satışta", default=True)  # available -> is_active olarak değişti
    is_featured = models.BooleanField("Öne Çıkan", default=False)  # featured -> is_featured olarak değişti
    meta_title = models.CharField("Meta Başlık", max_length=200, blank=True)  # Yeni eklendi
    meta_description = models.TextField("Meta Açıklama", blank=True)  # Yeni eklendi
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})