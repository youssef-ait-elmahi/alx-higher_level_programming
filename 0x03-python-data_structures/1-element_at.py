#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 > idx > (my_list):
        return None
    if len(my_list) < idx:
        return None
    else:
        return (my_list[idx])
