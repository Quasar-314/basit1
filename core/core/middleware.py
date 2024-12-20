# core/middleware.py
from django.http import HttpResponseForbidden
import re

class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # SQL injection koruması
        if self._check_sql_injection(request):
            return HttpResponseForbidden("Forbidden")
            
        # XSS koruması
        if self._check_xss(request):
            return HttpResponseForbidden("Forbidden")
            
        response = self.get_response(request)
        
        # Güvenlik başlıkları
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        
        return response
        
    def _check_sql_injection(self, request):
        sql_patterns = [
            r'(\s|^)(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER)(\s|$)',
            r'--',
            r';',
            r'\/\*.*\*\/',
        ]
        
        for param in request.GET.values():
            for pattern in sql_patterns:
                if re.search(pattern, param, re.I):
                    return True
        return False
        
    def _check_xss(self, request):
        xss_patterns = [
            r'<script.*?>.*?<\/script>',
            r'javascript:',
            r'onerror=',
            r'onload=',
        ]
        
        for param in request.GET.values():
            for pattern in xss_patterns:
                if re.search(pattern, param, re.I):
                    return True
        return False
    
class IPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            request.ip_address = x_forwarded_for.split(',')[0]
        else:
            request.ip_address = request.META.get('REMOTE_ADDR')
            
        response = self.get_response(request)
        return response