
#list stores multiple values in single variable.
#add, remove items in the lists
#list are ordered , it means items are added to the end.

fruits = ["Bananan", "Orange", "Kiwi"]

more_fruits = []

def pavailablefruits():
    print("Fruits Available : ")
    for x in fruits:
        print(x)

mf = input("You Want to add more fruits (Y/N) : ")
nm = input("How Many Fruits You Want To Add : ")
i = 0
mfruits = {}

if mf.upper() == "Y":
    while i < int(nm):
        mfruits = input ("Enter New Fruits (" + str(i) + ") :")
        more_fruits.append(mfruits)
        i += 1

fruits = fruits + more_fruits
pavailablefruits()
