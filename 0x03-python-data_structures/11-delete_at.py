#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    helper = my_list[:]
    if len(my_list) <= idx or idx < 0:
        return my_list
    else:
        del (helper[idx])
    return helper


delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 0
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)