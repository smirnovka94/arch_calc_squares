from django import template

register = template.Library()


@register.filter
def after_last_underscore(value):
    if '_' in value:
        return value.rsplit('_', 1)[-1]
    return value

@register.filter
def sort_list_by_name(value):
    return value.order_by('name')

@register.filter
def sort_list_by_number(value):
    return value.order_by('number')