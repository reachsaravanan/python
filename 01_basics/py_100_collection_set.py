my_fruits: set = {"Banana", "Orange", "Apple", "Kiwi"}
my_brothers_fruits: set = {"Kiwi", "Berry", "Graphs", "Apple"}

print(f'My Favorites Fruits\t\t\t: {my_fruits}')
print(f'My Brother Favorites Fruits\t: {my_brothers_fruits}')
print(f'Fruits both Liked\t\t\t: {my_fruits.intersection(my_brothers_fruits)}')
print(f'Fruits i Don\'t Like\t\t\t: {my_brothers_fruits.difference (my_fruits)}')
print(f'Fruits brother Don\'t Like\t: {my_fruits.difference (my_brothers_fruits)}')

my_brothers_fruits.difference_update(my_fruits)

print(f'My Favorites Fruits\t\t\t: {my_fruits}')
print(f'My Brother Favorites Fruits\t: {my_brothers_fruits}')

my_brothers_fruits.remove("Berry")
my_brothers_fruits.pop()

print(f'My Favorites Fruits\t\t\t: {my_fruits}')
print(f'My Brother Favorites Fruits\t: {my_brothers_fruits}')

my_brothers_fruits.add("Water Melon")
my_brothers_fruits.add("Dragon Fruit")

print(f'My Favorites Fruits\t\t\t: {my_fruits}')
print(f'My Brother Favorites Fruits\t: {my_brothers_fruits}')