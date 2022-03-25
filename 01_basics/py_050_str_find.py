"""
Accept file name from user and print only file extension
"""

user_file = input("Enter Your File Name with Extension :")
if "." in user_file:
    file_extension = user_file.split(".")
    print(f'The Split list\t\t: {file_extension}')
    print(f'The File Name\t\t: {file_extension[0]}')
    print(f'The File Extension\t: {file_extension[-1]}')
    print(f'The File Extension\t: {repr(file_extension[-1])}')
    print(f'Full File Name\t\t: {file_extension[0]}.{file_extension[-1]}')
    print(repr.__doc__)
else:
    print("Invalid File")