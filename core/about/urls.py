# about/urls.py
from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
]