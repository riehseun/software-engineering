# Uses python3
import sys
import math


def get_number_of_inversions(a, inversion):
    """
    Implements mergesort and count the number of inversions

    Args:
    a -- input array
    inversion -- an array where the first element is the number of
                 inversion

    Returns:
    (mergedm inversion) -- sorted array and number of inversion
    """

    if len(a) == 1:
        return (a, inversion)

    if len(a) == 2:
        # If wrong order, swap
        if a[0] > a[1]:
            temp = a[0]
            a[0] = a[1]
            a[1] = temp
            inversion[0] += 1

        return (a, inversion)

    mid = math.floor(len(a)/2)

    lower = get_number_of_inversions(a[:mid], inversion)[0]
    upper = get_number_of_inversions(a[mid:len(a)], inversion)[0]
    merged = []

    i = 0
    j = 0
    upper_emptied_out = False
    while i < len(lower):
        if lower[i] > upper[j] and upper_emptied_out == False:
            while lower[i] > upper[j]:
                inversion[0] += (len(lower)-i)
                merged.append(upper[j])
                if j < len(upper)-1:
                    j += 1
                else:
                    upper_emptied_out = True
                    break

            merged.append(lower[i])
            i += 1
        else:
            merged.append(lower[i])
            i += 1

    while j < len(upper) and upper_emptied_out == False:
        merged.append(upper[j])
        j += 1

    return (merged, inversion)


print(get_number_of_inversions([2,3,9,2,9], [0]))
print(get_number_of_inversions([9, 8, 7, 3, 2, 1], [0]))