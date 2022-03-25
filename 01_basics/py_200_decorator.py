"""
Multiple decorator
"""


def decorator_1(function):
    def inner():
        temp_str = 'decorator-1\n' + function()
        return temp_str
    return inner


def decorator_2(function: object) -> object:
    def inner():
        temp_str = 'Decorator-2\n' + function()
        return temp_str
    return inner


def decorator_3(function):
    def inner():
        temp_str = 'decorator-3\n' + function()
        return temp_str
    return inner


@decorator_2
@decorator_3
@decorator_1
def display():
    return "Hello World"


print(display())
