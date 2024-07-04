#!/usr/bin/python3
"""Algorithms for list of integers."""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
