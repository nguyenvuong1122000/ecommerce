from django import template
register = template.Library()
import locale
locale.setlocale(locale.LC_ALL, '')


@register.filter
def modulo(num, val):
    return num % val

@register.simple_tag
def string_format(str):
    return str[:25] + "..."

@register.simple_tag
def format_value(val):
    return locale.currency(val, grouping=True)

