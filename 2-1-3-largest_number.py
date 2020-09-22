#Uses python3
import sys


def largest_number(a):
    """
    Calculates the largest number that can be constructed with
    the numbers from input list

    Args:
    a -- input list of numbers

    Returns:
    largest_number -- the largest number that can be constructed with
                      the numbers from input list
    """

    array = new_quick_sort(a)

    largest_number = ""

    for number in array:
        largest_number += str(number)

    return largest_number


def new_quick_sort(a):
    """
    Implements a new quick sort where a custom logic is used to compare
    two numbers

    Args:
    a -- input list of numbers

    Returns:
    output list of sorted numbers
    """

    if len(a) <= 1:
        return a

    pivot = a[0]
    partition1 = []
    partition2 = []

    for i in range(1,len(a)):

        u = str(a[i]) + str(pivot)
        v = str(pivot) + str(a[i])

        if u > v:
            partition1.append(a[i])
        else:
            partition2.append(a[i])


    return (new_quick_sort(partition1)
           + [pivot]
           + new_quick_sort(partition2))


print(largest_number([21,2]))
print(largest_number([9,4,6,1,9]))
print(largest_number([23,39,92]))