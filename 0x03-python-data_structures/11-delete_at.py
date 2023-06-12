#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        helper = my_list[:]
        if idx < 0 or len(my_list) <= idx:
            return my_list
        else:
            del (helper[idx])
        return helper
