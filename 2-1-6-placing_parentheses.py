def evalt(i, j, op, M, m):
    """
    Finds the maximum and minimum values by going through all possible
    cases

    Args:
    i -- index to start
    j -- index to end
    op -- all operations
    M -- 2-dimensional array containing maximum values
    m -- 2-dimensional array containing minimum values

    Returns:
    The minimum and maximum values
    """

    minimum = 100000000
    maximum = -100000000

    for k in range(i,j):
        if op[k] == "+":
            a = M[i][k] + M[k+1][j]
            b = M[i][k] + m[k+1][j]
            c = m[i][k] + M[k+1][j]
            d = m[i][k] + m[k+1][j]
        elif op[k] == "-":
            a = M[i][k] - M[k+1][j]
            b = M[i][k] - m[k+1][j]
            c = m[i][k] - M[k+1][j]
            d = m[i][k] - m[k+1][j]
        elif op[k] == "*":
            a = M[i][k] * M[k+1][j]
            b = M[i][k] * m[k+1][j]
            c = m[i][k] * M[k+1][j]
            d = m[i][k] * m[k+1][j]

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return (minimum, maximum)


def get_maximum_value(dataset):
    """
    Finds the maximum value of an arithmetic expression by specifying
    the order of applying parentheses

    Args:
    dataset -- an arithmetic expression

    Returns:
    The maximum value after applying aprentheses
    """

    d = []
    op = []

    for i in range(len(dataset)):
        if i % 2 == 0:
            d.append(int(dataset[i]))
        else:
            op.append(dataset[i])

    n = len(d)

    M = [[0 for i in range(n)] for j in range(n)]
    m = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])

    for s in range(n-1):
        for i in range(n-s-1):
            j = i + s + 1
            m[i][j], M[i][j] = evalt(i, j, op, M, m)

    return M[0][n-1]


print(get_maximum_value("1+5"))
print(get_maximum_value("5-8+7*4-8+9"))
