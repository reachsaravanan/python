def py_002_ut_odd_even(lst, remainder):
    temp_list = []
    for x in lst:
        if x % 2 == remainder:
            temp_list.append(x)
    return temp_list
