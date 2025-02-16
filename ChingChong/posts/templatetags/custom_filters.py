from django import template
from django.db.models import Count

register = template.Library()

@register.filter
def count_rating(queryset, rating):
    if queryset:
        return len( queryset.filter(rating=rating) )
    return 0    
