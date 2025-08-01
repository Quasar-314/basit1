# Generated by Django 5.1.4 on 2024-12-18 16:50

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, "Değerlendirme 1'den küçük olamaz"), django.core.validators.MaxValueValidator(5, "Değerlendirme 5'ten büyük olamaz")], verbose_name='Değerlendirme')),
                ('comment', models.TextField(verbose_name='Yorum')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Onaylı')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Müşteri Yorumu',
                'verbose_name_plural': 'Müşteri Yorumları',
                'ordering': ['-created_at'],
            },
        ),
    ]
