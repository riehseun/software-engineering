# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    """
    Computes nth Fibonacci (which is large) mod m

    Args:
    n -- nth Fibonacci sequence
    m -- number to mod the nth Fibonacci sequence

    Returns:
    nth Fibonacci mod m
    """

    if n <= 1:
        return n

    k = n % get_pisano_period_length(m)
    if k == 0:
        return 0

    # Initialize array to store Fibonacci sequence
    fib_array = []
    fib_array.append(0)
    fib_array.append(0)
    for _ in range(2,k):
        fib_array.append(0)

    fib_array[0] = 1
    fib_array[1] = 1
    for i in range(2, k):
        fib_array[i] = (fib_array[i-1] + fib_array[i-2]) % m

    number = fib_array[k-1]
    return number


def get_pisano_period_length(m):
    """
    Computes the length of pisano period

    Args:
    m -- input integer

    Returns:
    length of pisano period
    """

    current = 1
    previous = 1

    for i in range(1, m*m):
        temp = previous
        previous = current % m
        current = (current + temp) % m

        if current == 1 and previous == 0:
            return i+1


print(get_fibonacci_huge_naive(239, 1000))
print(get_fibonacci_huge_naive(2816213588, 239))