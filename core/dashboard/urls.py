from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    # Ana dashboard URL'leri
    path('login/', views.DashboardLoginView.as_view(), name='dashboard_login'),
    path('', views.dashboard_home, name='home'),
    path('about/edit/', views.about_edit, name='dashboard_about_edit'),
    path('messages/', views.messages_list, name='dashboard_messages'),
    path('gallery/', views.gallery_list, name='dashboard_gallery'),
    path('media-mentions/', views.media_mentions_list, name='dashboard_media_mentions'),
    path('carousel/', views.carousel_list, name='dashboard_carousel'),
    path('categories/', views.categories_list, name='dashboard_categories'),
    path('products/', views.products_list, name='dashboard_products'),
    path('logout/', views.DashboardLogoutView.as_view(), name='logout'),

    # Hizmet URL'leri
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    
    # Ekip URL'leri
    path('team/', views.team_member_list, name='team_member_list'),
    path('team/create/', views.team_member_create, name='team_member_create'),
    path('team/<int:pk>/edit/', views.team_member_edit, name='team_member_edit'),
    path('team/<int:pk>/delete/', views.team_member_delete, name='team_member_delete'),

    # Medya Bahsetmeleri CRUD
    path('media-mentions/add/', views.media_mention_add, name='dashboard_media_mention_add'),
    path('media-mentions/<int:pk>/edit/', views.media_mention_edit, name='dashboard_media_mention_edit'),
    path('media-mentions/<int:pk>/delete/', views.media_mention_delete, name='dashboard_media_mention_delete'),
    
    # Galeri CRUD
    path('gallery/add/', views.gallery_add, name='dashboard_gallery_add'),
    path('gallery/<int:pk>/edit/', views.gallery_edit, name='dashboard_gallery_edit'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='dashboard_gallery_delete'),
    
    
    
    
    # Kategori ve ürün URL'leri
    path('categories/', views.categories_list, name='dashboard_categories'),
    path('categories/add/', views.category_add, name='dashboard_category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='dashboard_category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='dashboard_category_delete'),
    path('categories/<int:category_id>/products/', views.category_products, name='dashboard_category_products'),
    
    path('products/', views.products_list, name='dashboard_products'),
    path('products/add/', views.product_add, name='dashboard_product_add'),
    path('products/<int:pk>/edit/', views.product_edit, name='dashboard_product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='dashboard_product_delete'),
    
        
    
    
    
    
    # İletişim mesajları için URL'ler
    path('messages/', views.messages_list, name='dashboard_messages'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),

    # Müşteri yorumları için URL'ler
    path('reviews/', views.review_list, name='reviews'),
    path('reviews/toggle/<int:id>/', views.review_status_toggle, name='review_toggle'),
    path('reviews/delete/<int:id>/', views.review_delete, name='review_delete'),
    
    # Carousel CRUD
    path('carousel/add/', views.carousel_add, name='dashboard_carousel_add'),
    path('carousel/<int:pk>/edit/', views.carousel_edit, name='dashboard_carousel_edit'),
    path('carousel/<int:pk>/delete/', views.carousel_delete, name='dashboard_carousel_delete'),
]