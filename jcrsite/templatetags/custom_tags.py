from django import template
import re

register = template.Library()

#Used to split the messy inputs based on the empty line gaps and returns a neater list of strings
@register.filter
def serveryItems(value):
    output = re.sub(r'\n+', '#', value)
    output = output.split('#')
    return output
