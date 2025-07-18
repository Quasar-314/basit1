# Generated by Django 5.1.4 on 2024-12-14 17:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='content',
        ),
        migrations.AddField(
            model_name='about',
            name='mission',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Misyonumuz'),
        ),
        migrations.AddField(
            model_name='about',
            name='story',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Hikayemiz'),
        ),
        migrations.AddField(
            model_name='about',
            name='vision',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Vizyonumuz'),
        ),
        migrations.AlterField(
            model_name='about',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Görsel'),
        ),
        migrations.AlterField(
            model_name='about',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama'),
        ),
        migrations.AlterField(
            model_name='about',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
