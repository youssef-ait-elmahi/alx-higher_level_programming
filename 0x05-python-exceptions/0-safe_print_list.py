#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    while printed < x:
        try:
            print('{}'.format(my_list[printed]), end='')
        except IndexError:
            break
        printed += 1
    print()
    return printed
