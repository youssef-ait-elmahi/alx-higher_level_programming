#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    helper = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            helper += 1
        except IndexError:
            break
    print(end='\n')
    return(helper)


safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
