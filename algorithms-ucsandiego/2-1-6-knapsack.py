import sys


def optimal_weight(W, weights):
    """
    Solving classical knapsack problem where weights == values and
    same items cannot be drawn more than once

    Args:
    W -- total weight
    weights -- list of all available weights

    Returns:
    Optimal value
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

    return v[W][n]


print(optimal_weight(10, [1,4,8]))
