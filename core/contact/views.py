from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from reviews.forms import ReviewForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def contact(request):
    contact_form = ContactForm()
    review_form = ReviewForm()
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'contact':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.ip_address = get_client_ip(request)
                contact.save()
                messages.success(request, 'Mesajınız başarıyla gönderildi.')
                return redirect('contact:contact')
                
        elif form_type == 'review':
            review_form = ReviewForm(request.POST, request.FILES)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.ip_address = get_client_ip(request)
                review.save()
                messages.success(request, 'Değerlendirmeniz başarıyla alındı. İncelendikten sonra yayınlanacaktır.')
                return redirect('contact:contact')
    
    context = {
        'contact_form': contact_form,
        'review_form': review_form
    }
    return render(request, 'contact/contact.html', context)  # Bu satır eklendi