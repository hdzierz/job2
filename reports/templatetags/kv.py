from django import template

register = template.Library()

@register.filter(name='kv')
def kv(d, key):
    if key in d:
        return d[key]
    else:
        return 'NA'

