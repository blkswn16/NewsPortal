from django import template

register = template.Library()

@register.filter()
def censor(value):
    bad_words = ('редиска!', 'дурак', 'тупица', 'блин', 'оладушек', 'пипец')

    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")

    for i in value.split():
        if i.lower() in bad_words:
            value = value.replace(i, f"{i[0]}{'*' * (len(i) - 2)}{i[-1]}")
    return value
