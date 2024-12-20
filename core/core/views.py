# contact/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm, ReviewForm
from .models import Review

def contact(request):
    reviews = Review.objects.all().order_by('-created_at')[:5]
    
    if request.method == 'POST':
        if 'form_type' in request.POST:
            if request.POST['form_type'] == 'contact':
                contact_form = ContactForm(request.POST)
                review_form = ReviewForm()
                if contact_form.is_valid():
                    contact_form.save()
                    messages.success(request, 'Mesajınız başarıyla gönderildi.')
                    return redirect('contact:contact')
            
            elif request.POST['form_type'] == 'review' and request.user.is_authenticated:
                review_form = ReviewForm(request.POST)
                contact_form = ContactForm()
                if review_form.is_valid():
                    review = review_form.save(commit=False)
                    review.user = request.user
                    review.save()
                    messages.success(request, 'Değerlendirmeniz başarıyla kaydedildi.')
                    return redirect('contact:contact')
    else:
        contact_form = ContactForm()
        review_form = ReviewForm()

    context = {
        'contact_form': contact_form,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'contact/contact.html', context)