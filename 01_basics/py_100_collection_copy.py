"""
Accept comma separated number's input from user
and create list/tuple and store those users inputs.
"""

print ("""
==> List       is ordered   , changeable    , duplicate allowed
==> Dictionary is ordered   , changeable    , No duplicate
==> Tuple      is ordered   , unchangeable  , duplicate Allowed.
==> Set        is unordered , unchangeable  , No duplicate and un-indexed.
""")

user_input = "1,2,3,4"
print(f'User Input\t: {user_input}')

try:
    user_list = user_input.split(",")
except BaseException as err:
    print(f'Unexpected ERROR\t: {err=}')
else:
    print(f'User input copied to list\t: {user_list}')

try:
    user_tuple = tuple(user_list)
except BaseException as err:
    print(f'Unexpected ERROR\t: {err=}')
else:
    print(f'User List copied to Tuple\t: {user_tuple}')

try:
    user_set = set(user_list)
except BaseException as err:
    print(f'Unexpected ERROR\t: {err=}')
else:
    print(f'User List copied to Set\t\t: {user_set}')

try:
    user_dict: dict = {}
    user_dict = dict(user_list)
except BaseException as err:
    print(f'User List copied to dict\t: {err=}')
else:
    print(f'User List copied to dict\t: {user_dict}')