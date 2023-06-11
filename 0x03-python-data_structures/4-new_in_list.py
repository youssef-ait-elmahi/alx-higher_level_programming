#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list[:]
    if 0 > idx:
        return my_list.copy()

    elif len(my_list) <= idx:
        return my_list.copy()
    else:
        cp_list[idx] = element
        my_list = cp_list
        return cp_list
