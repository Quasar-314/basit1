# gallery/urls.py
from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
]