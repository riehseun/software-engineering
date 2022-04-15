import sys


def lcs2(a, b):
    """
    Finds the length of a longest common subsequence of two sequences

    Args:
    a -- first input string
    a -- second input string

    Returns:
    The length of a longest common subsequence
    """

    n = len(a)
    m = len(b)

    # Create 2-dimensional distance matrix D
    D = []

    for i in range(n+1):
        D.append([])

    for i in range(n+1):
        for _ in range(m+1):
            D[i].append(0)

    for j in range(1,m+1):
        for i in range(1,n+1):

            # If there was a match where both index i and j were smaller
            # than the current index i and j, that match indicates
            # construction of a valid substring
            if a[i-1] == b[j-1]:
                D[i][j] = find_the_max_from_small_indexes(D, i, j) + 1

    # Find the maximum number from the table
    potential_max = []
    for i in range(1,len(D)):
        for j in range(1,len(D[0])):
            potential_max.append(D[i][j])

    return max(potential_max)


def find_the_max_from_small_indexes(D, a, b):
    """
    Finds the maximum number from the values of 2-dimensional array
    whose indexes are less than a and b

    Args:
    D -- 2-dimensional array
    a -- an index
    b -- an index

    Returns:
    The maximum number from the table
    """

    maximum = 0

    for i in range(a):
        for j in range(b):
            if D[i][j] > maximum:
                maximum = D[i][j]

    return maximum


print(lcs2("275", "25"))
print(lcs2("7", "1234"))
print(lcs2("2783", "5287"))
