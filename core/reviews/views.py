from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg
from .models import Review
from .forms import ReviewForm

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Yorumunuz başarıyla alındı. İncelendikten sonra yayınlanacaktır.')
            return redirect('home:index')
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'title': 'Yorum Ekle'
    }
    return render(request, 'reviews/review_form.html', context)

def review_list(request):
    reviews = Review.objects.filter(is_approved=True).select_related('user')
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    # Sayfalama
    paginator = Paginator(reviews, 10)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    
    context = {
        'reviews': reviews,
        'average_rating': round(average_rating, 1) if average_rating else 0,
        'title': 'Müşteri Yorumları'
    }
    return render(request, 'reviews/review_list.html', context)