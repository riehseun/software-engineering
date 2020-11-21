def edit_distance(s, t):
    """

    """

    n = len(s)
    m = len(t)

    # Initialize 2-dimensional distance matrix D
    D = []

    for i in range(n):
        D.append([])

    for i in range(n):
        for _ in range(m):
            D[i].append(0)

    for i in range(n):
        D[i][0] = i

    for j in range(m):
        D[0][j] = j

    for j in range(m):
        for i in range(n):

            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1

            if s[i] == t[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[n-1][m-1]
    # potential_max = []
    # for i in range(len(D)):
    #     potential_max.append(max(D[i]))
    # return max(potential_max)


# print(edit_distance("ab", "ab"))
# print(edit_distance("short", "ports"))
# print(edit_distance("editing", "distance"))

if __name__ == "__main__":
    print(edit_distance(input(), input()))
