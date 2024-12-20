# gallery/models.py
from django.db import models
from django.urls import reverse

class Gallery(models.Model):
    MEDIA_TYPES = (
        ('image', 'Resim'),
        ('video', 'Video'),
    )
    
    title = models.CharField("Başlık", max_length=200)
    description = models.TextField("Açıklama", blank=True)
    media_type = models.CharField("Medya Tipi", max_length=5, choices=MEDIA_TYPES)
    image = models.ImageField("Resim", upload_to='gallery/%Y/%m/', blank=True)
    video = models.FileField("Video Dosyası", upload_to='gallery/videos/%Y/%m/', blank=True,
                           help_text="MP4, WebM formatlarını destekler")
    video_url = models.URLField("Video URL", blank=True, help_text="YouTube veya Vimeo URL'si")
    is_featured = models.BooleanField("Öne Çıkan", default=False)  # featured -> is_featured olarak değişti
    is_active = models.BooleanField("Aktif", default=True)
    order = models.PositiveIntegerField("Sıralama", default=0)
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)  # Yeni eklendi

    class Meta:
        verbose_name = "Galeri"
        verbose_name_plural = "Galeri"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:gallery_detail', kwargs={'pk': self.pk})