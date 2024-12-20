# gallery/templatetags/video_tags.py
from django import template
import re

register = template.Library()

@register.filter
def youtube_id(url):
    pattern = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else ''

@register.filter
def vimeo_id(url):
    pattern = r'(?:vimeo\.com\/)(\d+)'
    match = re.search(pattern, url)
    return match.group(1) if match else ''