n=int(input("Numarul de l/c:"))
M=[[1 for i in range(n)] for j in range(n)]
for i in range(n-2,-1,-1):
    for j in range(n-2,-1,-1):
        M[i][j]=M[i+1][j]+M[i][j+1]
for linie in M:
    print(*linie)
