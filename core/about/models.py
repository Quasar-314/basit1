# about/models.py
from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField("Başlık", max_length=200)
    short_description = models.TextField("Kısa Açıklama", null=True, blank=True)
    mission = RichTextField("Misyonumuz", null=True, blank=True)
    vision = RichTextField("Vizyonumuz", null=True, blank=True)
    story = RichTextField("Hikayemiz", null=True, blank=True)
    image = models.ImageField("Görsel", upload_to='about/', null=True, blank=True)
    years_experience = models.PositiveIntegerField("Tecrübe (Yıl)", default=20)
    completed_jobs = models.PositiveIntegerField("Tamamlanan İşler", default=5000)
    happy_customers = models.PositiveIntegerField("Mutlu Müşteriler", default=1000)
    meta_title = models.CharField("Meta Başlık", max_length=200, blank=True)
    meta_description = models.TextField("Meta Açıklama", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hakkımızda"
        verbose_name_plural = "Hakkımızda"

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField("Başlık", max_length=200)
    description = models.TextField("Açıklama")
    image = models.ImageField("Resim", upload_to='services/', help_text="Hizmet için görsel")
    order = models.IntegerField("Sıralama", default=0)
    is_active = models.BooleanField("Aktif", default=True)
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"
        ordering = ['order']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField("Ad Soyad", max_length=100)
    position = models.CharField("Pozisyon", max_length=100)
    bio = models.TextField("Biyografi", blank=True)
    image = models.ImageField("Fotoğraf", upload_to='team/')
    order = models.IntegerField("Sıralama", default=0)
    is_active = models.BooleanField("Aktif", default=True)
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    class Meta:
        verbose_name = "Ekip Üyesi"
        verbose_name_plural = "Ekip Üyeleri"
        ordering = ['order']

    def __str__(self):
        return self.name