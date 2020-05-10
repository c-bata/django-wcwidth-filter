from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.text import Truncator
from wcwidth import wcswidth as func_wcswidth
from wcwidth import wcwidth as func_wcwidth

register = Library()


@register.filter(is_safe=True)
@stringfilter
def truncate_wcswidth(value, arg):
    try:
        width = int(arg)
    except ValueError:  # Invalid literal for int().
        return value  # Fail silently.

    if not isinstance(value, str):
        return ""  # Fail silently.

    max_chars, chars, sum_width = len(value), 0, 0
    for char in value:
        sum_width += func_wcwidth(char)
        if sum_width >= width and chars != max_chars - 1:
            break
        chars += 1
    return Truncator(value).chars(chars)


@register.filter(is_safe=False)
def wcswidth(value):
    if not isinstance(value, str):
        return 0
    return func_wcswidth(value)
