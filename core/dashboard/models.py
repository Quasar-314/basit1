# dashboard/models.py
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# dashboard/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class DashboardSettings(models.Model):
    site_title = models.CharField(_('Site Başlığı'), max_length=200)
    favicon = models.ImageField(_('Favicon'), upload_to='settings/', blank=True)
    logo = models.ImageField(_('Logo'), upload_to='settings/', blank=True)
    email = models.EmailField(_('E-posta'), blank=True)
    phone = models.CharField(_('Telefon'), max_length=20, blank=True)
    address = models.TextField(_('Adres'), blank=True)
    facebook = models.URLField(_('Facebook'), blank=True)
    twitter = models.URLField(_('Twitter'), blank=True)
    instagram = models.URLField(_('Instagram'), blank=True)
    linkedin = models.URLField(_('LinkedIn'), blank=True)
    youtube = models.URLField(_('YouTube'), blank=True)
    analytics_code = models.TextField(_('Analytics Kodu'), blank=True)
    meta_title = models.CharField(_('Meta Başlık'), max_length=200, blank=True)
    meta_description = models.TextField(_('Meta Açıklama'), blank=True)
    created_at = models.DateTimeField(_('Oluşturulma Tarihi'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True)

    class Meta:
        verbose_name = _('Site Ayarı')
        verbose_name_plural = _('Site Ayarları')

    def __str__(self):
        return self.site_title

class Message(models.Model):
    STATUS_CHOICES = (
        ('new', _('Yeni')),
        ('read', _('Okundu')),
        ('replied', _('Yanıtlandı')),
        ('spam', _('Spam')),
    )

    name = models.CharField(_('İsim'), max_length=100)
    email = models.EmailField(_('E-posta'))
    subject = models.CharField(_('Konu'), max_length=200)
    message = models.TextField(_('Mesaj'))
    status = models.CharField(_('Durum'), max_length=10, choices=STATUS_CHOICES, default='new')
    note = models.TextField(_('Not'), blank=True)
    created_at = models.DateTimeField(_('Gönderim Tarihi'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True)

    class Meta:
        verbose_name = _('Mesaj')
        verbose_name_plural = _('Mesajlar')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


# dashboard/models.py'a eklenecek
class MediaMention(models.Model):
    title = models.CharField("Başlık", max_length=200)
    source = models.CharField("Kaynak", max_length=100)
    url = models.URLField("URL", blank=True)
    publish_date = models.DateField("Yayın Tarihi")  # publication_date -> publish_date olarak değişti
    description = models.TextField("Açıklama", blank=True)
    image = models.ImageField("Görsel", upload_to='media_mentions/%Y/%m/', blank=True)
    is_active = models.BooleanField("Aktif", default=True)  # Yeni eklendi
    order = models.IntegerField("Sıralama", default=0)  # Yeni eklendi
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)  # Yeni eklendi
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)  # Yeni eklendi

    class Meta:
        verbose_name = "Basın Haberi"
        verbose_name_plural = "Basın Haberleri"
        ordering = ['order', '-publish_date']

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategori Adı')
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(verbose_name='Açıklama', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Aktif')

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategori')
    name = models.CharField(max_length=200, verbose_name='Ürün Adı')
    slug = models.SlugField(max_length=220, unique=True)
    description = RichTextField(verbose_name='Açıklama')
    image = models.ImageField(upload_to='products/%Y/%m/', verbose_name='Ürün Görseli')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Fiyat')
    stock = models.IntegerField(verbose_name='Stok Durumu')
    is_featured = models.BooleanField(default=False, verbose_name='Öne Çıkan')
    is_active = models.BooleanField(default=True, verbose_name='Satışta')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class CustomerReview(models.Model):
    name = models.CharField(_("Müşteri Adı"), max_length=100)
    review = models.TextField(_("Yorum"))
    rating = models.IntegerField(_("Puan"), choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(_("Yorum Tarihi"), auto_now_add=True)
    is_approved = models.BooleanField(_("Onaylı"), default=False)

    class Meta:
        verbose_name = _("Müşteri Yorumu")
        verbose_name_plural = _("Müşteri Yorumları")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}/5"
    
