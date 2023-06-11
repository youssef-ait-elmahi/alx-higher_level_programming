#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 > idx:
        my_list = new_list
        return(new_list)

    if len(my_list) <= idx:
        my_list = new_list
        return(new_list)
    else:
        new_list = ''
        new_list = my_list[:]
        new_list[idx] = element
        return(new_list)
