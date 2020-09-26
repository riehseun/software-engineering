# Uses python3
import sys
import random


def randomized_quick_sort(a):
    """
    Implement quicksort algorithm with 3 partitions

    Args:
    a -- input array

    Return:
    sorted array
    """

    # Corner case
    if len(a) == 0:
        return a

    pivot = a[0]
    lower = []
    upper = []
    same = []

    for elem in a:
        if elem < pivot:
            lower.append(elem)
        elif elem == pivot:
            same.append(elem)
        else:
            upper.append(elem)

    return randomized_quick_sort(lower) + same + randomized_quick_sort(upper)


print(randomized_quick_sort([2,3,9,2,2]))
print(randomized_quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))