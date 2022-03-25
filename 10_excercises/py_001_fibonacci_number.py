"""
Fibonacci Series
[0,1,1,2,3,5,8,13,21,34.....]
"""

def show_fibonacci(first_num, max_num):
    result = 0
    next_num = 1
    for i in range(max_num):
        yield result
        result = first_num + next_num
        first_num = next_num
        next_num = result


a = 0
b = 1
c = 0
fibonacci_series = ""
for i in range(10):
    fibonacci_series = fibonacci_series + str(c) + ","
    c = a + b
    a = b
    b = c
print(f'Fibonacci Series\t{fibonacci_series}')

fibonacci_series = ""
for i in show_fibonacci(0, 10):
    fibonacci_series = fibonacci_series + str(i) + ","
print(f'Fibonacci Series\t{fibonacci_series}')

