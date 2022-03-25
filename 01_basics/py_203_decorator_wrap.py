from functools import wraps


def basic_decorator(function):
    count = 0

    @wraps(function)  # Python built-in decorator
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("Function Name {0}".format(inner.__name__))
        print("Function Doc {0}".format(inner.__doc__))
        print("Function Count {0}".format(count))
        return function(*args, **kwargs)

    inner.__name__ = function.__name__
    inner.__doc__ = function.__doc__
    return inner


@basic_decorator
def addition(a, b, c):
    """
    :param a: :param b: :param c:
    This function add three parameter and return sum.
    """
    return a + b + c


print(addition(1, 2, 3))
