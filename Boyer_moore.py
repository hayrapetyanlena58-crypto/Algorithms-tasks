def boyer_moore(T, P):
    n = len(T)
    m = len(P)

    L = {}
    for j in range(m):
        L[P[j]] = j

    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0:
            if T[i + j] != P[j]:
                break
            j -= 1

        if j == -1:
            return f"Found at position {i}"
        else:
            i += max(1, j - L.get(T[i + j], -1))

    return "FAIL"


T = "ABAAABCD"
P = "ABC"

print(boyer_moore(T, P))
