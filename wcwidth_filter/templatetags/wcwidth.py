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

    truncated = False
    sum_width, chars = 0, 0
    ellipsis_width = func_wcwidth("…")
    last = len(value) - 1
    for i, char in enumerate(value):
        sum_width += func_wcwidth(char)

        if i == last and sum_width == width:
            break

        if sum_width + ellipsis_width > width:
            truncated = True
            break
        chars += 1

    return value[:chars] + "…" if truncated else value


@register.filter(is_safe=False)
def wcswidth(value):
    if not isinstance(value, str):
        return 0
    return func_wcswidth(value)
