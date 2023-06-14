#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for key in a_dictionary:
        new_d[key] = a_dictionary[key] * 2
    return(new_d)
