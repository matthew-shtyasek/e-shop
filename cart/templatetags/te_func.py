from django.template import Library

register = Library()


#  {{ cart|get_item:pk }}
@register.filter
def get_item(d: dict, key):
    return d[str(key)]


@register.filter
def prod_count(d: dict):
    return sum(map(int, list(d.values())))
# получаем из словаря значения (values)
# преобразовываем их в список (list)
# затем в int (map)
# и суммируем (sum)
