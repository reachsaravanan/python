# Pythons data types

first_name = {}
last_name = {}
age = 0
weight = 0
guest_list = {}
guest_tuple = {}
guest_range = {}
guest_dict = {}
guest_set = {}
guest_frozen_set = {}


def set_guest_data():
    global first_name
    global last_name
    global age
    global weight
    global guest_list
    global guest_tuple
    global guest_range
    global guest_dict
    global guest_set
    global guest_frozen_set

    first_name = 'Saravanan'
    last_name = 'Balakrishnan'
    age = 45
    weight = 68.5

    guest_list = ["Saravanan", "Balakrishnan", 45, 69.5]
    guest_tuple = ("Saravanan", "Balakrishnan", 45, 69.5)
    guest_range = range(4)
    guest_dict = {"first_name": "Saravanan", "last_name": "Balakrishnan", "Age": "45", "Weight": "69.5"}
    guest_set = {"Saravanan", "Balakrishnan", 45, 69.5}
    guest_frozen_set = {"Saravanan", "Balakrishnan", 45, 69.5}


def get_guest_data():
    txt = "Data Type Of [ {0} ] is [ {1} ]"
    print(txt.format(first_name, type(first_name)))
    print(txt.format(last_name, type(last_name)))
    print(txt.format(age, type(age)))
    print(txt.format(weight, type(weight)))
    print(txt.format(guest_list, type(guest_list)))
    print(txt.format(guest_tuple, type(guest_tuple)))
    print(txt.format(guest_range, type(guest_range)))
    print(txt.format(guest_dict, type(guest_dict)))
    print(txt.format(guest_set, type(guest_set)))
    print(txt.format(guest_frozen_set, type(guest_frozen_set)))


set_guest_data()
get_guest_data()
