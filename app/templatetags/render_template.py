from django import template

register = template.Library()

@register.simple_tag
def render_template(request, name, module=None):
    if module is None:
        module = request.module
    return module.render_template(request, name)