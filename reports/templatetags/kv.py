from django import template

register = template.Library()

@register.filter(name='kv')
def kv(d, key):
    if isinstance(d, dict):
        if key in d:
            return d[key]
        else:
            return 'NA'
    elif isinstance(d, object):
        return getattr(d, key)


@register.filter(name='coln')
def coln(col):
    col = col.replace("__name", "")
    col = col.replace("__company", "")

    buff = col.split('__')
    if len(buff) > 1:
        buff.pop(0)
    col = '__'.join(buff)

    return ''.join(x for x in col.title() if x != '_')
    
