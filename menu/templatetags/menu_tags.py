from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent').prefetch_related('children')
    return {'menu_items': menu_items, 'path': path, 'request': request}
