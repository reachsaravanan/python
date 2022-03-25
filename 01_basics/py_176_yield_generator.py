import itertools


def add_number(x):
    return x + 1
    return x + 2
    return x + 3


def generator_func(x):
    x += 1
    yield x
    x += 2
    yield x
    x += 3
    yield x


def generator_loop(max_num):
    for i in range(max_num):
        yield i


def exp_nums(value):
    result = value
    yield result
    while True:
        result = result * value
        yield result


def coroutines_example():
    print("My First Co-Routine")
    try:
        while True:
            value = (yield)
            print(value)
    except GeneratorExit:
        print("Exiting Co-routine")

print(f'FAILED To Print Multiple Return Output From Function\t\t: {add_number(0)}')
print(f'FAILED To Print Multiple Return Output From Function\t\t: {add_number(0)}')

x = generator_func(10)
print(f'FAILED To Print Multiple YIELD Output From Function\t\t\t: {str(x.__next__())}')
print(f'FAILED To Print Multiple YIELD Output From Function\t\t\t: {str(x.__next__())}')
print(f'FAILED To Print Multiple YIELD Output From Function\t\t\t: {str(x.__next__())}')

output_text = ""
iterable_obj = iter(generator_func(10))
for item in iterable_obj:
    output_text += str(item) + ","
print(f'Convert Generator Output as Iterable Object (for loop)\t\t: {output_text}')

output_text = ""
for item in generator_func(10):
    output_text += str(item) + ","

print(f'Print YIELD Generator Output\t\t\t\t\t\t\t\t: {output_text}')

output_text = ""
iterable_obj = iter(generator_loop(10))
for item in iterable_obj:
    output_text += str(item) + ","
print(f'Print YIELD LOOP Generator Output\t\t\t\t\t\t\t: {output_text}')

# Define generator to print exponent of 2
print(f'Print YIELD Exponential Generator\t\t\t\t\t\t\t: {list(itertools.islice(exp_nums(2), 10))}')

# co-routine is like function but it accepts
coroutine_obj = coroutines_example()
next(coroutine_obj)
coroutine_obj.send("My First Input")


# write generator expression that gives all number below 100 that is divisible by 3 and 5.
output_text = ""
for x in range(100):
    if x % 3 == 0 and x % 5 == 0:
        output_text = output_text + str(x) + ","
print(f'Print number below 100 that is divisible by (3 and 5)\t\t: {output_text}')

output_text = ""
gen_obj = (x for x in range(100) if x % 3 == 0 and x % 5 == 0)
for x in gen_obj:
    output_text = output_text + str(x) + ","
print(f'Print number below 100 that is divisible by (3 and 5)\t\t: {output_text}')

