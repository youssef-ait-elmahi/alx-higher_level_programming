#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    helper = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            helper += 1
        except (TypeError, ValueError):
            continue
    print('')
    return helper
