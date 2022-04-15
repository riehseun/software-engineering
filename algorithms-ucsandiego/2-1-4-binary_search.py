# Uses python3
import sys
import math


def binary_search(a, x):
    """
    Implements binary search on a sorted array

    Args:
    a -- sorted array
    x -- list of values to search for in the array "a"

    Returns:
    result -- list of indexes of searched values
    """

    result = ""

    for i in x:
        result += str(do_search(a, 0, len(a)-1, i))
        result += " "

    return result[:-1]


def do_search(a, low, high, i):
    """
    Implements binary search on a sorted array

    Args:
    a -- sorted array
    low -- min value of array "a"
    high -- max value of array "a"
    i -- the value to look for in the array "a"

    Returns:
    the index of searched value
    """

    if low > high:
        return -1

    mid = math.floor(low + (high-low)/2)

    if i == a[mid]:
        return mid
    elif i < a[mid]:
        return do_search(a, low, mid-1, i)
    else:
        return do_search(a, mid+1, high, i)


print(binary_search([1,5,8,12,13], [8,1,23,1,11]))