#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    helper = my_list[:]
    if len(my_list) < idx or idx < 0:
        return my_list
    else:
        del helper[idx]
        return helper
