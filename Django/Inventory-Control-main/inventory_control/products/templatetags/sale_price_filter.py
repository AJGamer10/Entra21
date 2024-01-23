from django import template
import re

register = template.Library()

@register.filter(name="format_sale_price")
def format_sale_price(value):
    value = str(value)
    sale_price_pattern = r"(\d+)[,.](\d{2})"
    
    match = re.match(sale_price_pattern, value)
    if match:
        return "R${},{}".format(*match.groups())
    
    return value