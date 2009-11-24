from django.template import Library
register = Library()

@register.filter
def mod(value, arg):
    "Returns the modulo of the args"
    return value % arg

@register.filter
def gt(value, arg):
    "Returns a boolean of whether the value is greater than the argument"
    return value > int(arg)

@register.filter
def lt(value, arg):
    "Returns a boolean of whether the value is less than the argument"
    return value < int(arg)

@register.filter
def gte(value, arg):
    "Returns a boolean of whether the value is greater than or equal to the argument"
    return value >= int(arg)

@register.filter
def lte(value, arg):
    "Returns a boolean of whether the value is less than or equal to the argument"
    return value <= int(arg)

@register.filter
def length_gt(value, arg):
    "Returns a boolean of whether the value's length is greater than the argument"
    return len(value) > int(arg)

@register.filter
def length_lt(value, arg):
    "Returns a boolean of whether the value's length is less than the argument"
    return len(value) < int(arg)

@register.filter
def length_gte(value, arg):
    "Returns a boolean of whether the value's length is greater than or equal to the argument"
    return len(value) >= int(arg)

@register.filter
def length_lte(value, arg):
    "Returns a boolean of whether the value's length is less than or equal to the argument"
    return len(value) <= int(arg)
