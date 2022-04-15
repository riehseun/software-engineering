# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    """
    Computes the last digit of squared sum up to nth Fibonacci

    Args:
    n -- nth Fibonacci sequence

    Returns:
    last digit of squared sum up to nth Fibonacci
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

    # Initialize array to store squared Fibonacci sequence
    fib_array_squared = []
    fib_array_squared.append(0)
    fib_array_squared.append(0)
    for _ in range(2, k+2):
        fib_array_squared.append(0)

    fib_array[0] = 1
    fib_array[1] = 1
    fib_array_squared[0] = 1
    fib_array_squared[1] = 2
    for i in range(2, k+2):
        fib_array[i] = (fib_array[i-1] + fib_array[i-2]) % 10
        fib_array_squared[i] = fib_array[i]**2 + fib_array_squared[i-1]

    number = fib_array_squared[k-1] % 10
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


print(fibonacci_sum_squares_naive(7))
print(fibonacci_sum_squares_naive(73))
print(fibonacci_sum_squares_naive(1234567890))