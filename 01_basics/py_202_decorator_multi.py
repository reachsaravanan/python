def decorator_1(function):
    def inner(*a):
        x = function(*a)
        final_x = x * 10
        print('Final X :',final_x)
        return final_x
    return inner


def decorator_2(function):
    def inner(*b):
        y = function(*b)
        final_y = y * 7 + 3
        print('Final Y :',final_y)
        return final_y
    return inner


@decorator_2
@decorator_1
def my_first_function(x, y):
    return x - y


@decorator_1
@decorator_2
def my_next_function(x, y):
    return x - y


my_first_function(12, 2)
my_next_function(12, 2)


