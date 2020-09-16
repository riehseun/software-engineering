# Uses python3
import sys


def fibonacci_partial_sum_naive(m, n):
    """
    Computes the last digit of partial sum up to nth Fibonacci

    Args:
    n -- nth Fibonacci sequence
    m -- mth Fibonacci sequence

    Returns:
    last digit of partial sum up to nth Fibonacci
    """

    if m == 0:
        j = 0
    else:
        j = fibonacci_sum_naive(m-1)

    i = fibonacci_sum_naive(n)


    if i == j:
        return i
    elif i > j:
        return i-j
    else:
        return i+10-j


def fibonacci_sum_naive(n):
    """
    Computes the last digit of sum up to nth Fibonacci

    Args:
    n -- nth Fibonacci sequence

    Returns:
    last digit of sum up to nth Fibonacci
    """

    if n <= 1:
        return n

    k = n % get_pisano_period_length(10)
    if k == 0:
        return 0

    # Initialize array to store Fibonacci sequence
    fib_array = []
    fib_array.append(0)
    fib_array.append(0)
    for _ in range(2, k+2):
        fib_array.append(0)

    fib_array[0] = 1
    fib_array[1] = 1
    for i in range(2, k+2):
        fib_array[i] = (fib_array[i-1] + fib_array[i-2]) % 10

    if fib_array[k+1] == 0:
        number = 9
    else:
        number = fib_array[k+1] - 1

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


print(fibonacci_partial_sum_naive(3, 7))
print(fibonacci_partial_sum_naive(10, 10))
print(fibonacci_partial_sum_naive(10, 200))