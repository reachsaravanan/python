output_text = ""
for item in range(10,20):
    output_text += str(item)
    output_text += ","
print(f'Range object (for loop)\t\t\t\t\t\t: {output_text}')

iterable_val = "Hari Ram"
iterable_object = iter(iterable_val)
output_text = ""
for i in range(100):
    try:
        item = next(iterable_object)
        output_text += str(item)
    except StopIteration:
        break
print(f'Iterable/Iterator Object (for loop)\t\t\t: {output_text}')

output_text = ""
iterable_object = iter(iterable_val)
while True:
    try:
        item = next(iterable_object)
        output_text += str(item)
    except StopIteration:
        break
print(f'Iterable/Iterator Object (while loop)\t\t: {output_text}')


class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1
        return x


output_text = ""
for item in Test(20):
    output_text = output_text + str(item)
    output_text += ","
print(f'Iterable/Iterator Object (Class/Object) \t: {output_text}')
