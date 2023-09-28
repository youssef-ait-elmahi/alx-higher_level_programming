#!/usr/bin/python3
def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mid = length // 2
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
       list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
