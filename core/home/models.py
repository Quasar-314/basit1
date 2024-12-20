# home/models.py
from django.db import models
from django.core.exceptions import ValidationError

class CarouselSlide(models.Model):
    title = models.CharField("Başlık", max_length=200)
    description = models.TextField("Açıklama")
    image = models.ImageField("Görsel", upload_to='carousel/')
    button_text = models.CharField("Buton Metni", max_length=50, blank=True)
    button_url = models.CharField("Buton URL", max_length=200, blank=True)
    order = models.PositiveIntegerField("Sıralama", default=0)
    is_active = models.BooleanField("Aktif", default=True)
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Carousel Slayt"
        verbose_name_plural = "Carousel Slaytlar"

    def __str__(self):
        return self.title

    def clean(self):
        if self.is_active:
            active_slides = CarouselSlide.objects.filter(is_active=True)
            if self.pk:
                active_slides = active_slides.exclude(pk=self.pk)
            if active_slides.count() >= 5:
                raise ValidationError('En fazla 5 aktif slayt olabilir.')