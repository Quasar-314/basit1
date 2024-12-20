# products/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category

def product_list(request):
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_active=True)  # available -> is_active
    else:
        products = Product.objects.filter(is_active=True)  # Zaten doğru
    
    # Sayfalama
    paginator = Paginator(products, 9)  # Her sayfada 9 ürün
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category if category_slug else None
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)  # available -> is_active
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)