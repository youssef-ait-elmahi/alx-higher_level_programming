#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    index = 0
    while index < list_length:
        c = 0
        try:
            c = my_list_1[index] / my_list_2[index]
        except (TypeError, ValueError):
            c = 0
            print('wrong type')
        except ZeroDivisionError:
            c = 0
            print('division by 0')
        except IndexError:
            c = 0
            print('out of range')
        finally:
            new_list[index] = c
        index += 1
    return new_list
