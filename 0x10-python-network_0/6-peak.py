#!/usr/bin/python3
"""
This module contains a function that finds the peak of an
unsorted list.
"""


def find_peak(list_of_integers):
    """This function finds the peak of an insorted list"""
    lst = list_of_integers
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    if len(list_of_integers) == 2:
        return (max(list_of_integers))
    if list_of_integers[0] > list_of_integers[1]:
        return (list_of_integers[0])
    if list_of_integers[len(lst) - 1] > list_of_integers[len(lst) - 2]:
        return (list_of_integers[len(list_of_integers) - 1])
    start = 1
    end = len(lst)
    mid = (end - start) / 2
    for mid in range(start, end):
        if lst[mid] > lst[mid - 1]:
            if lst[mid] > lst[mid + 1]:
                return lst[mid]
            start = mid + 1
            mid = (end - start) / 2
        elif lst[mid] == lst[mid - 1]:
            if mid == end:
                return lst[mid]
            if mid == start:
                return (lst[mid])
            if lst[mid] > lst[mid + 1]:
                mid = mid - 1
            else:
                mid = mid - 1
        else:
            end = mid - 1
            mid = (end - start) / 2
