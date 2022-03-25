"""
Accept one number (N) from user and calculate N+NN+NN = 5+55+555=615
"""

user_number = input("Enter Your Number :")
user_number_1 = int("%s" % user_number)
user_number_2 = int("%s%s" % (user_number, user_number))
user_number_3 = int("%s%s%s" % (user_number, user_number, user_number))
print(f'Calculated Result \t : {user_number_1}\t+\t{user_number_2}\t+\t{user_number_3}\t=\t', user_number_1+user_number_2+user_number_3)
