# dashboard/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MediaMention, CustomerReview
from .forms import (MediaMentionForm, CategoryForm, ProductForm, 
                   CustomerReviewForm, AboutForm, GalleryForm,
                   CarouselSlideForm)
from about.models import About
from gallery.models import Gallery
from contact.models import Contact
from home.models import CarouselSlide
from products.models import Category, Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from about.models import Service, TeamMember
from .forms import ServiceForm, TeamMemberForm
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from reviews.models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Login View
class DashboardLoginView(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True
    next_page = 'dashboard:home'

# Dashboard Ana Sayfa
@login_required
def dashboard_home(request):
    context = {
        'total_products': Product.objects.count(),
        'total_categories': Category.objects.count(),
        'total_reviews': CustomerReview.objects.count(),
        'total_media_mentions': MediaMention.objects.count(),
        'recent_products': Product.objects.order_by('-created_at')[:5],
        'recent_reviews': CustomerReview.objects.order_by('-created_at')[:5],
        'unread_messages': Contact.objects.filter(is_read=False).count(),
    }
    return render(request, 'dashboard/index.html', context)

# Hakkımızda Bölümü
@login_required
def about_edit(request):
    about = About.objects.first()
    if request.method == 'POST':
        print("POST isteği alındı")
        print("POST verileri:", request.POST)
        
        form = AboutForm(request.POST, request.FILES, instance=about)
        print("Form oluşturuldu")
        
        if form.is_valid():
            print("Form geçerli")
            print("Form temizlenmiş veriler:", form.cleaned_data)
            try:
                saved_about = form.save()
                print("Form başarıyla kaydedildi, kaydedilen veriler:", {
                    'title': saved_about.title,
                    'short_description': saved_about.short_description,
                    'mission': saved_about.mission,
                    'vision': saved_about.vision,
                    'story': saved_about.story,
                    'years_experience': saved_about.years_experience,
                    'completed_jobs': saved_about.completed_jobs,
                    'happy_customers': saved_about.happy_customers,
                })
                messages.success(request, 'Hakkımızda bilgileri güncellendi.')
                return redirect('dashboard_home')
            except Exception as e:
                print("Kaydetme hatası:", str(e))
                messages.error(request, f'Kaydetme hatası: {str(e)}')
        else:
            print("Form geçersiz")
            print("Form hataları:", form.errors)
    else:
        form = AboutForm(instance=about)
        print("GET isteği, mevcut veriler:", {
            'title': about.title if about else None,
            'short_description': about.short_description if about else None,
            'mission': about.mission if about else None,
            'vision': about.vision if about else None,
            'story': about.story if about else None,
            'years_experience': about.years_experience if about else None,
            'completed_jobs': about.completed_jobs if about else None,
            'happy_customers': about.happy_customers if about else None,
        })
    
    return render(request, 'dashboard/about/edit.html', {'form': form, 'about': about})

# Mesajlar ve Yorumlar
@login_required
def messages_list(request):
    contact_messages = Contact.objects.all().order_by('-created_at').values(
        'id', 'name', 'email', 'phone', 'subject', 'message', 
        'created_at', 'is_read'  # ip_address buradan çıkarıldı
    )
    customer_reviews = CustomerReview.objects.all().order_by('-created_at')
    
    # Okunma durumunu güncelle
    unread_messages = Contact.objects.filter(is_read=False)
    for message in unread_messages:
        message.is_read = True
        message.save()
    
    context = {
        'contact_messages': contact_messages,
        'customer_reviews': customer_reviews,
        'unread_count': Contact.objects.filter(is_read=False).count()
    }
    return render(request, 'dashboard/messages/list.html', context)

# dashboard/views.py'a ekleyin
@login_required
def message_delete(request, pk):
    message = get_object_or_404(Contact, pk=pk)
    message.delete()
    messages.success(request, 'Mesaj başarıyla silindi.')
    return redirect('dashboard:dashboard_messages')

# Galeri Yönetimi
@login_required
def gallery_list(request):
    form = GalleryForm()
    galleries = Gallery.objects.all().order_by('-created_at')
    return render(request, 'dashboard/gallery/list.html', {
        'galleries': galleries,
        'form': form
    })

@login_required
def gallery_add(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Galeri öğesi eklendi.')
            return redirect('dashboard_gallery')
    else:
        form = GalleryForm()
    return render(request, 'dashboard/gallery/add.html', {'form': form})

@login_required
def gallery_edit(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, 'Galeri öğesi güncellendi.')
            return redirect('dashboard_gallery')
    else:
        form = GalleryForm(instance=gallery)
    return render(request, 'dashboard/gallery/edit.html', {'form': form, 'gallery': gallery})

@login_required
def gallery_delete(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    gallery.delete()
    messages.success(request, 'Galeri öğesi silindi.')
    return redirect('dashboard_gallery')

# Basın Bölümü
@login_required
def media_mentions_list(request):
    mentions = MediaMention.objects.all().order_by('-publish_date')
    form = MediaMentionForm()
    return render(request, 'dashboard/media_mentions/list.html', {
        'mentions': mentions,
        'form': form
    })

@login_required
def media_mention_add(request):
    if request.method == 'POST':
        form = MediaMentionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Basın haberi başarıyla eklendi.')
            return redirect('dashboard:dashboard_media_mentions')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = MediaMentionForm()
    return render(request, 'dashboard/media_mentions/add.html', {'form': form})

@login_required
def media_mention_edit(request, pk):
    mention = get_object_or_404(MediaMention, pk=pk)
    if request.method == 'POST':
        form = MediaMentionForm(request.POST, request.FILES, instance=mention)
        if form.is_valid():
            form.save()
            messages.success(request, 'Basın haberi güncellendi.')
            return redirect('dashboard_media_mentions')
    else:
        form = MediaMentionForm(instance=mention)
    return render(request, 'dashboard/media_mentions/edit.html', {'form': form, 'mention': mention})

@login_required
def media_mention_delete(request, pk):
    mention = get_object_or_404(MediaMention, pk=pk)
    mention.delete()
    messages.success(request, 'Basın haberi silindi.')
    return redirect('dashboard_media_mentions')

# Kategori Yönetimi
@login_required
def categories_list(request):
    categories = Category.objects.all().order_by('name')
    form = CategoryForm()
    return render(request, 'dashboard/categories/list.html', {
        'categories': categories,
        'form': form
    })

@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori eklendi.')
            return redirect('dashboard_categories')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/categories/add.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori güncellendi.')
            return redirect('dashboard_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/categories/edit.html', {'form': form, 'category': category})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Kategori silindi.')
    return redirect('dashboard_categories')

# Ürün Yönetimi
@login_required
def products_list(request):
    # Filtreleme için kategori ve durumu al
    category_id = request.GET.get('category')
    status = request.GET.get('status')
    search = request.GET.get('search')
    
    # Başlangıç queryset'i
    products = Product.objects.select_related('category').all()
    
    # Filtreleme uygula
    if category_id:
        products = products.filter(category_id=category_id)
    if status == 'active':
        products = products.filter(is_active=True)
    elif status == 'inactive':
        products = products.filter(is_active=False)
    if search:
        products = products.filter(name__icontains=search)
    
    # Sıralama
    products = products.order_by('-created_at')
    
    # Kategorileri getir (filtre için)
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'dashboard/products/list.html', context)

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ürün eklendi.')
            return redirect('dashboard_products')
    else:
        form = ProductForm()
    return render(request, 'dashboard/products/add.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ürün güncellendi.')
            return redirect('dashboard_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/products/edit.html', {'form': form, 'product': product})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Ürün silindi.')
    return redirect('dashboard_products')

# Carousel Yönetimi
@login_required
def carousel_list(request):
    slides = CarouselSlide.objects.all().order_by('order')
    form = CarouselSlideForm()
    return render(request, 'dashboard/carousel/list.html', {
        'slides': slides,
        'form': form
    })

@login_required
def carousel_add(request):
    if request.method == 'POST':
        form = CarouselSlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slayt eklendi.')
            return redirect('dashboard_carousel')
    else:
        form = CarouselSlideForm()
    return render(request, 'dashboard/carousel/add.html', {'form': form})

@login_required
def carousel_edit(request, pk):
    slide = get_object_or_404(CarouselSlide, pk=pk)
    if request.method == 'POST':
        form = CarouselSlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slayt güncellendi.')
            return redirect('dashboard_carousel')
    else:
        form = CarouselSlideForm(instance=slide)
    return render(request, 'dashboard/carousel/edit.html', {'form': form, 'slide': slide})

@login_required
def carousel_delete(request, pk):
    slide = get_object_or_404(CarouselSlide, pk=pk)
    slide.delete()
    messages.success(request, 'Slayt silindi.')
    return redirect('dashboard_carousel')


# dashboard/views.py (mevcut views'lara ekleyin)

@login_required
def review_add(request):
    if request.method == 'POST':
        form = CustomerReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yorum eklendi.')
            return redirect('dashboard_messages')
    else:
        form = CustomerReviewForm()
    return render(request, 'dashboard/reviews/add.html', {'form': form})

@login_required
def review_edit(request, pk):
    review = get_object_or_404(CustomerReview, pk=pk)
    if request.method == 'POST':
        form = CustomerReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yorum güncellendi.')
            return redirect('dashboard_messages')
    else:
        form = CustomerReviewForm(instance=review)
    return render(request, 'dashboard/reviews/edit.html', {'form': form, 'review': review})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(CustomerReview, pk=pk)
    review.delete()
    messages.success(request, 'Yorum silindi.')
    return redirect('dashboard_messages')


@login_required
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    form = ProductForm()  # Yeni ürün eklemek için boş form
    
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'form': form
    }
    return render(request, 'dashboard/categories/products_list.html', context)




# Hizmet views
@login_required
def service_list(request):
    services = Service.objects.all().order_by('order')
    return render(request, 'dashboard/services/list.html', {'services': services})

@login_required
def service_create(request):
    if request.method == 'POST':
        # request.FILES eklendi
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Hizmet başarıyla eklendi.')
            return redirect('dashboard:service_list')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = ServiceForm()
    return render(request, 'dashboard/services/form.html', {'form': form, 'title': 'Yeni Hizmet Ekle'})

@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        # request.FILES eklendi
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Hizmet başarıyla güncellendi.')
            return redirect('dashboard:service_list')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dashboard/services/form.html', {'form': form, 'title': 'Hizmet Düzenle'})

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, 'Hizmet başarıyla silindi.')
    return redirect('dashboard:service_list')

# Ekip views
@login_required
def team_member_list(request):
    team_members = TeamMember.objects.all().order_by('order')
    return render(request, 'dashboard/team/list.html', {'team_members': team_members})

@login_required
def team_member_create(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ekip üyesi başarıyla eklendi.')
            return redirect('dashboard:team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'dashboard/team/form.html', {'form': form, 'title': 'Yeni Ekip Üyesi Ekle'})

@login_required
def team_member_edit(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=team_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ekip üyesi başarıyla güncellendi.')
            return redirect('dashboard:team_member_list')
    else:
        form = TeamMemberForm(instance=team_member)
    return render(request, 'dashboard/team/form.html', {'form': form, 'title': 'Ekip Üyesi Düzenle'})

@login_required
def team_member_delete(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    team_member.delete()
    messages.success(request, 'Ekip üyesi başarıyla silindi.')
    return redirect('dashboard:team_member_list')


class DashboardLogoutView(LogoutView):
    template_name = 'dashboard/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    


 


@login_required(login_url='dashboard:dashboard_login')
def review_list(request):
    # Pagination eklemek için
    page = request.GET.get('page', 1)
    reviews_list = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews_list, 10)  # Her sayfada 10 yorum
    
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    
    return render(request, 'dashboard/reviews/list.html', {'reviews': reviews})




@login_required
def review_status_toggle(request, id):
    if request.method == 'POST':
        review = get_object_or_404(Review, id=id)
        review.is_approved = not review.is_approved
        review.save()
        status = "onaylandı" if review.is_approved else "onayı kaldırıldı"
        messages.success(request, f'Yorum başarıyla {status}.')
        return redirect('dashboard:reviews')
    return redirect('dashboard:reviews')

@login_required(login_url='dashboard:dashboard_login')
def review_delete(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    messages.success(request, 'Yorum silindi.')
    return redirect('dashboard:reviews')