#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    helper = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            helper.append(True)
        else:
            helper.append(False)
    return helper
