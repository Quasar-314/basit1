# home/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_range')
def get_range(value):
    """
    Rating sayısı kadar yıldız göstermek için range oluşturur
    """
    try:
        return range(int(value))
    except (TypeError, ValueError):
        return range(0)

@register.filter
def divide_into_groups(items, group_size):
    """
    Verilen listeyi belirtilen boyutta gruplara böler
    """
    if not items:
        return []
    
    try:
        groups = []
        for i in range(0, len(items), group_size):
            groups.append(items[i:i + group_size])
        return groups
    except (TypeError, ValueError):
        return []