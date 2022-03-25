user_input = "1,2,3,4"

try:
    print(f'User Input\t: {user_input}')

    user_list = user_input.split(",")
    print(f'User input copied to list\t: {user_list}')

    user_tuple = tuple(user_list)
    print(f'User List copied to Tuple\t: {user_tuple}')

    user_set = set(user_list)
    print(f'User List copied to Set\t: {user_set}')

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
    raise
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
else:
    print("Completed Successfully")
