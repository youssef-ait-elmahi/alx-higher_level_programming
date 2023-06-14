#!/usr/bin/python3
def uniq_add(my_list=[]):
    helper = set(my_list)
    result = 0
    for i in helper:
        result += i
    return(result)
