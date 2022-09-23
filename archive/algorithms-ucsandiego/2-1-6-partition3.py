import sys
from random import shuffle


def partition3(A):
    """
    Find if numbers in the input array A can be evenly split between
    3 batches

    Args:
    A -- input array

    Returns:
    1 if it can be splited. 0 Otherwise
    """

    if sum(A) % 3 != 0:
        return 0

    num_try = 10
    while num_try > 0:

        # Copy array by value
        array = A[:]

        # Answer could be different based on the arrangement of array
        shuffle(array)

        ret_val = compute_partition3(array)

        if ret_val == 0:
            num_try -= 1
        else:
            return 1

    return 0


def optimal_weight(W, weights):
    """
    Solving classical knapsack problem where weights == values and
    same items cannot be drawn more than once

    Args:
    W -- total weight
    weights -- list of all available weights

    Returns:
    Table containing all the steps computing classical knapsack
    """

    # In this problem, the values and weights are the same
    n = len(weights)
    v = [[0 for i in range(n+1)] for w in range(W+1)]

    # Initialize values
    for i in range(n+1):
        v[0][i] = 0

    for w in range(W+1):
        v[w][0] = 0

    for i in range(1, n+1):
        for w in range (1, W+1):
            v[w][i] = v[w][i-1]

            if weights[i-1] <= w:
                val = v[w-weights[i-1]][i-1] + weights[i-1]
                if v[w][i] < val:
                    v[w][i] = val

    return v


def reconstruct_knapsack(W, n, A, v):
    """
    Reconstructs the solution of knapsack problem

    Args:
    v -- table containing all the steps computing classical knapsack

    Returns:
    An array containing solutions to the knapsack problem
    """

    # Reconstrut the solution
    sol = []
    w = W
    for i in reversed(range(1, n+1)):
        # If item i was used
        if v[w][i] == v[w-A[i-1]][i-1] + A[i-1]:
            sol.append(A[i- 1])
            w = w-A[i-1]

    return sol


def compute_partition3(A):
    """
    Find if numbers in the input array A can be evenly split between
    3 batches

    Args:
    A -- input array

    Returns:
    1 if it can be splited. 0 Otherwise
    """

    # Set the total weight as one-thrid of the total sum because each
    # batch cannot exceed this
    W = int(sum(A)/3)

    n = len(A)

    # Compute classical knapsack
    v = optimal_weight(W, A)

    # If the solution of the classical knapsack turns out to be exactly
    # W then, at least one batch can be constructed with exactly by
    # one-thrid of the total value of input array A
    if v[W][n] != W:
        return 0

    sol = reconstruct_knapsack(W, n, A, v)

    # Remove the solution for the first batch from the input list
    for item in sol:
        if item in A:
            A.remove(item)

    # Update the length of A since A has been changed
    n = len(A)

    # Compute classical knapsack again
    v = optimal_weight(W, A)

    if v[W][n] != W:
        return 0

    # n, A, v are changed which will result in different solution
    sol = reconstruct_knapsack(W, n, A, v)

    # Remove the solution for the second batch from the updated list A
    for item in sol:
        if item in A:
            A.remove(item)

    # If the sum of the remaining (third) batch equals to W, then all
    # three batches can be divided equally
    if sum(A) == W:
        return 1
    else:
        return 0


print(partition3([3,3,3,3]))
print(partition3([40]))
print(partition3([17,59,34,57,17,23,67,1,18,2,59]))
print(partition3([1,2,3,4,5,5,7,7,8,10,12,19,25]))
