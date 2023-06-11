#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 > idx:
        return my_list

    if len(my_list) <= idx:
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list


replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(my_list)
print(new_list)
