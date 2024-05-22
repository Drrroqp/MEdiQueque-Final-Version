from django import template
from mq.models import *

register = template.Library()

@register.simple_tag()
def get_category():
    return Category.objects.all()