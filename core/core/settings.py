# core/settings.py

import os
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')  # .env dosyasından alınacak

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

  # Prodüksiyonda değiştirilecek
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=lambda v: [s.strip() for s in v.split(',')])


# SSL/HTTPS ayarları
SECURE_SSL_REDIRECT = not DEBUG  # Production'da HTTPS'e yönlendir
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 yıl
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CSRF koruması
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://localhost,http://127.0.0.1', 
                             cast=lambda v: [s.strip() for s in v.split(',')])

# XSS koruması
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'



# Password hashing
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Application definition
INSTALLED_APPS = [
    # Mevcut uygulamalar...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    
    # Oluşturduğumuz uygulamalar
    'home.apps.HomeConfig',
    'products.apps.ProductsConfig',
    'gallery.apps.GalleryConfig',
    'about.apps.AboutConfig',
    'contact.apps.ContactConfig',
    'dashboard.apps.DashboardConfig',  # Yeni eklenen dashboard uygulaması
    'reviews.apps.ReviewsConfig',

    
    # Üçüncü parti uygulamalar
    'ckeditor',
    'crispy_forms',
    'django_cleanup.apps.CleanupConfig',
    'compressor',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django_ratelimit.middleware.RatelimitMiddleware',
    'core.middleware.IPAddressMiddleware',
    


]

# Rate limiting ayarları
RATELIMIT_ENABLE = True
RATELIMIT_USE_CACHE = 'default'
RATELIMIT_VIEW = 'core.views.ratelimit_view'

ROOT_URLCONF = 'core.urls'

# core/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.seo_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Veritabanı yapılandırması
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Login URL'leri
LOGIN_URL = '/dashboard/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/dashboard/login/'  # Bu önemli
LOGOUT_URL = '/dashboard/logout/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60 * 24  # 24 saat
SESSION_COOKIE_SECURE = True
# Parola doğrulama
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Dil ve zaman ayarları
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik dosya ayarları
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Media dosyaları için
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms ayarı
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# CKEditor ayarları
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
    },
}

# Statik dosya sıkıştırma
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
    }
}

# Cache süreleri
CACHE_MIDDLEWARE_SECONDS = 300  # 5 dakika
CACHE_MIDDLEWARE_KEY_PREFIX = 'baran_anahtarci'


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail için
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='your-email@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='your-app-password')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='your-email@gmail.com')
CONTACT_EMAIL = config('CONTACT_EMAIL', default='your-email@gmail.com')





