# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """
    Solves classical Knapsack problem using greedy algorithm

    Args:
    capacity -- capacity of knapsack
    weights -- array of item weights
    values -- array of item values

    Returns:
    V -- total optimal value of Knapsack
    """

    num_items = len(weights)
    data_array = []

    for i in range(num_items):
        data_array.append([weights[i], values[i], values[i]/weights[i]])

    # sort by (value / weight) descending
    data_array.sort(key=lambda x: x[2], reverse=True)

    A = []
    for i in range(num_items):
        A.append(0)
    V = 0

    for i in range(num_items):
        if capacity == 0:
            return V
        a = min(data_array[i][0], capacity)
        V = V + a * data_array[i][1] / data_array[i][0]
        data_array[i][0] -= a
        A[i] += a
        capacity -= a

    return V


print(get_optimal_value(50, [20, 50, 30], [60, 100, 120]))
print(get_optimal_value(10, [30], [500]))