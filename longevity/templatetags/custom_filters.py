from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Fetches the value of the given key from the dictionary."""
    return dictionary.get(key)
