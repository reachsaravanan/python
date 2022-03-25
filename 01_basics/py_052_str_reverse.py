"""
Accept Users First and Last name
Print them in revers order with space between names.
"""
def f_reverse_string(i_name):
    i = len(i_name)
    r_name = ""
    while i > 0:
        i -= 1
        r_name = r_name + str(i_name[i])
    return r_name


first_name = input("Enter Your First Name :")
last_name = input("Enter Your Last Name :")
print("*" * 20)
print(f'User Input Name \t\t: {first_name} {last_name}')
print(f'Reversed Name By Code\t: {f_reverse_string(first_name)} {f_reverse_string(last_name)}')
print(f'Reversed Name By Slice[-1]\t: {first_name[::-1]} {last_name[::-1]}')
print(f'Reversed Name By Slice[-2]\t: {first_name[::-2]} {last_name[::-2]}')
print(f'User Input Name By Slice[1]\t: {first_name[::1]} {last_name[::1]}')
print(f'User Input Name By Slice[2]\t: {first_name[::2]} {last_name[::2]}')

print("*" * 20)