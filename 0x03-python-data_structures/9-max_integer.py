#!/usr/bin/python
def max_integer(my_list=[]):
    if not my_list:
        max_num = my_list[0]
        for num in my_list:
            if num > max_num:
                max_num = num
        return(max_num)
