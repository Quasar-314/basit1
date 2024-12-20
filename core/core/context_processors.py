# core/context_processors.py
def seo_context(request):
    """Global SEO context for all pages"""
    return {
        'default_meta_description': 'Baran Anahtarcı - 7/24 Profesyonel Anahtarcılık Hizmetleri',
        'default_meta_keywords': 'anahtarcı, çilingir, anahtar yapımı, kilit değişimi',
        'site_name': 'Baran Anahtarcı',
    }