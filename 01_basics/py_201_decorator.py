"""
decorator syntax
function_name = decorator_name(function_name)
        basic_function = basic_decorator(basic_function)
Otherwise, you can define it using @
        @basic_decorator
        def basic_function():
            pass
"""


def basic_decorator(function):
    count = 0

    def inner(*agrs, **kwargs):
        nonlocal count
        count += 1
        print('Function name is {0}'.format(inner.__name__))
        print('Function doc is {0}'.format(inner.__doc__))
        print('Function call count {0}'.format(count))
        return function(*agrs, **kwargs)

    inner.__name__ = function.__name__
    inner.__doc__ = function.__doc__
    return inner


def multiplay(a, b, c):
    """
    This function multiply 3 input value (a * b * c)
    """
    return a * b * c


@basic_decorator
def addition(a, b, c):
    """
    This function multiply 3 input value (a + b + c)
    """
    return a + b + c


print("Addition Result {0}".format(addition(1, 2, 3)))
multiplay = basic_decorator(multiplay)
print("Multiplication Result {0}".format(multiplay(1, 2, 3)))

