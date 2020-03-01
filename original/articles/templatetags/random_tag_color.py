import random
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@stringfilter
@register.simple_tag
def random_color():
    color_selection = ['layui-bg-red', 'ayui-bg-orange', 'layui-bg-cyan', 'layui-bg-blue']
    return mark_safe(random.choice(color_selection))
