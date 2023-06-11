#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 > idx:
        print(my_list)
    if len(my_list) <= idx:
        print(my_list)
    else:
        new_list = ''
        new_list = my_list[:]
        new_list[idx] = element
        print(new_list)
        print(my_list)
