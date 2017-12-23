from django import template
from django.db.models.aggregates import Count
from ..models import Story, Category

register = template.Library()

@register.simple_tag
def get_recent_storys(num=5):
    return Story.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_categories():
    
    return Category.objects.annotate(num_posts=Count('story')).filter(num_posts__gt=0)
