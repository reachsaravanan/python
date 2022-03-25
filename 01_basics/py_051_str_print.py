print("*" * 50)
print("Twinkle, twinkle, little star, "
      "\n\tHow I wonder what you are! "
      "\n\t\tUp above the world so high, "
      "\n\t\tLike a diamond in the sky. "
      "\nTwinkle, twinkle, little star, "
      "\n\tHow I wonder what you are!")

print("*" * 50)
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

print("*" * 50)
exam_date = (12, 12, 2022)
print(f'Exam Date\t: {exam_date}')
print("Formatted Examination Date : %i / %i / %i" % exam_date)


print("*" * 50)
user_input = "Hello Happy World"
print(f'User Input\t\t\t\t: {user_input}')
print(f'Show FIRST 5 Letters\t: {user_input[:5]}')
print(f'Remove LAST 5 Letters\t: {user_input[:-5]}')
print(f'Show MIDDLE 5 letters\t: {user_input[6:11]}')


print("*" * 50)

i = 0
father_name = "Saravanan,Balakrishnan"
mother_name = "Saraswath,Saravanan"
first_boy_name = "Shree Ram,Balakrishnan,Saravanan"
next_boy_name = "Shree Hari,Balakrishnan,Saravanan"

temp_name = ""
for x in father_name:
    temp_name = temp_name + str(x)
print(f'Father\\tt: {temp_name}')

temp_name = ""
while i < len(mother_name):
    temp_name = temp_name + mother_name[i]
    i += 1
print(f'Mother\t\t: {temp_name}')

print(f'First Boy\t: {first_boy_name}')
print(f'Next Boy\t: {next_boy_name}')


print("*" * 50)
print(f'Father last Name\t\t:{father_name.split(",")[-1]}')
print(f'First Boys Middle Name\t:{first_boy_name.split(",")[1]}')
print(f'Next Boys Middle Name\t:{next_boy_name.split(",")[1]}')