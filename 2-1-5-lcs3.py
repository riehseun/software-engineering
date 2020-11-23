import sys
import time


def lcs3(a, b, c):
    """
    Finds the length of a longest common subsequence of three sequences

    Args:
    a -- first input string
    a -- second input string
    c -- third input string

    Returns:
    The length of a longest common subsequence
    """

    n = len(a)
    m = len(b)
    p = len(c)

    # Create 3-dimensional distance matrix D
    D = [[[0 for k in range(p+1)] for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(1,p+1):

                # If there was a match where both index i and j were smaller
                # than the current index i and j, that match indicates
                # construction of a valid substring
                if a[i-1] == b[j-1] == c[k-1]:
                    D[i][j][k] = find_the_max_from_small_indexes(D, i, j, k)+1

    # Find the maximum number from the table
    maximum = 0
    for i in range(1,len(D)):
        for j in range(1,len(D[0])):
            for k in range(1,len(D[0][0])):
                if D[i][j][k] > maximum:
                    maximum = D[i][j][k]

    return maximum


def find_the_max_from_small_indexes(D, a, b, c):
    """
    Finds the maximum number from the values of 3-dimensional array
    whose indexes are less than a, b, and c

    Args:
    D -- 2-dimensional array
    a -- an index
    b -- an index

    Returns:
    The maxiumm number from the table
    """

    maximum = 0

    for i in reversed(range(a)):
        for j in reversed(range(b)):
            for k in reversed(range(c)):
                if D[i][j][k] != 0 and D[i][j][k] > maximum:
                    maximum = D[i][j][k]

    return maximum


# start_time = time.time()
# print(lcs3([1,2,3], [2,1,3], [1,3,5]))
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# print(lcs3([8,3,2,1,7], [8,2,1,3,8,10,7], [6,8,3,1,4,7]))
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# print(lcs3([3,1,2,5,7], [3,2,6,7], [3,1,2,6,7]))
# print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
