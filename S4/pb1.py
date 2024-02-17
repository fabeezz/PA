def matrice(n):
    M = [[i] + [0]*(i-1) for i in range(1, n)]
    M.append([i for i in range(n, 0, -1)])
    for i in range(n-2, 0, -1):
        for j in range(1, i+1):
            M[i][j] = M[i][j-1] + M[i+1][j-1] + M[i+1][j]
    return M
def afisare(M):
    ncmax = max([len(str(max(linie))) for linie in M])
    for linie in M:
        for elem in linie:
            print(str(elem).rjust(ncmax), end=' ')
        print()
M=matrice(5)
afisare(M)