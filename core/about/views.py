from django.shortcuts import render
from .models import About, Service, TeamMember
from dashboard.models import MediaMention

def about(request):
    about = About.objects.first()
    media_mentions = MediaMention.objects.filter(is_active=True).order_by('-publish_date')
    services = Service.objects.filter(is_active=True).order_by('order')
    team_members = TeamMember.objects.filter(is_active=True).order_by('order')
    
    context = {
        'about': about,
        'media_mentions': media_mentions,
        'services': services,
        'team_members': team_members,
        'company_info': {
            'years_experience': about.years_experience if about else 20,
            'completed_jobs': about.completed_jobs if about else 5000,
            'happy_customers': about.happy_customers if about else 1000,
            'services': Service.objects.filter(is_active=True).order_by('order'),
            'team_members': TeamMember.objects.filter(is_active=True).order_by('order'),
        }
    }
    return render(request, 'about/about.html', context)