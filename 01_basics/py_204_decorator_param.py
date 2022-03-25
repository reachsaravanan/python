"""
Passing paramters to decorators
"""


def my_decorator(*args, **kwargs):
    temp_list = []

    for i in args:
        temp_list.append(i)
    print('-'.join(temp_list))
    print("Inside my_decorator")
    print("Decorator Param via kwargs:", kwargs["param1"])

    def inner(func):
        def wrapper():
            return "<b><i>" + func() + "<\b><\i>"

        return wrapper

    return inner


# @my_decorator("These", "are", "args", param1 = "HARIRAM")
def my_func():
    return "Inside original my_func function"


print("TESTING MY CODE")
print(my_func())
