# Uses python3
import sys
import math


def get_majority_element(a):
    """
    Checks if the sequence contains an element that appears strictly
    more than n/2 times

    Args:
    a -- input array

    Returns:
    boolean indicating whether the check results in True/False
    """

    a.sort()

    mid = math.floor((len(a)-1)/2)

    if a.count(a[mid]) > len(a)/2:
        return True
    else:
        return False


print(get_majority_element([2,3,9,2,2]))
print(get_majority_element([1,2,3,4]))