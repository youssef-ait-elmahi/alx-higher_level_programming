#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    helper_1 = tuple_a + (0, 0)
    helper_2 = tuple_b + (0, 0)
    return (helper_1[0] + helper_2[0], helper_1[1] + helper_2[1])
