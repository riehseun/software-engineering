#Uses python3
import sys


def max_dot_product(a, b):
    """
    Calculates the maximum possible product from the elements of two
    input lists

    Args:
    a -- first list
    b -- second list

    Returns:
    result -- the maximum possible product
    """

    result = 0

    a_sorted = sorted(a, reverse=True)
    b_sorted = sorted(b, reverse=True)

    for i in range(len(a)):
        if a_sorted[i] > 0 and b_sorted[i] > 0:
            result += a_sorted[i] * b_sorted[i]
        else:
            break

    a_sorted = sorted(a)
    b_sorted = sorted(b)

    for i in range(len(a)):
        if a_sorted[i] < 0 and b_sorted[i] < 0:
            result += a_sorted[i] * b_sorted[i]
        else:
            break

    return result


print(max_dot_product([1, 3, -5], [-2, 4, 1]))
print(max_dot_product([1, 3, 5], [2, 4, 1]))