# stock/templatetags/stock_extras.py
from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """
    Multiplies the value by the arg.
    Usage: {{ price|mul:quantity }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''
