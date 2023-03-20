from django.template import Library

register = Library()


#  {{ cart|get_item:pk }}
@register.filter
def get_item(d: dict, key):
    return d[str(key)]


#  pk -> count