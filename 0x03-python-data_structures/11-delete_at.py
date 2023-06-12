#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    helper = my_list[:]
    if 0 > idx > len(my_list):
        return
    else:
        del helper[idx]
        return helper
