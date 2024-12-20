from .base import *

DEBUG = False
ALLOWED_HOSTS = ['www.barananahtarci.com', 'barananahtarci.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Statik dosya ayarları
STATIC_ROOT = '/var/www/barananahtarci.com/static/'
MEDIA_ROOT = '/var/www/barananahtarci.com/media/'

# Güvenlik ayarları
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True