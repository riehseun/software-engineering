def edit_distance(s, t):
    """
    Find the minimum number of operations (insertions, deletions, and
    substitutions of symbols) to transform one string into another

    Args:
    s -- first input string
    t -- second input string

    Returns:
    The minimum number of operations
    """

    n = len(s)
    m = len(t)

    # Create 2-dimensional distance matrix D
    D = []

    for i in range(n+1):
        D.append([])

    for i in range(n+1):
        for _ in range(m+1):
            D[i].append(0)

    # Initialize 2-dimensional distance matrix D
    for i in range(n+1):
        D[i][0] = i

    for j in range(m+1):
        D[0][j] = j

    for j in range(1,m+1):
        for i in range(1,n+1):

            # Recurrence
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1

            if s[i-1] == t[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[n][m]


print(edit_distance("ab", "ab"))
print(edit_distance("short", "ports"))
print(edit_distance("editing", "distance"))
