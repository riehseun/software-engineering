# Uses python3
import sys


def gcd_naive(a, b):
    """
    Implments efficient algorithm for finding the gretest common divisor

    Args:
    a -- numerator
    b -- denominator

    Returns:
    gretest common divisor
    """

    if b == 0:
        return a

    c = a % b

    return gcd_naive(b, c)


print(gcd_naive(18, 35))
print(gcd_naive(28851538, 1183019))