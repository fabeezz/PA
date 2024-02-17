def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b , a%b)
n=5
mat=[[1 if gcd(i+1,j+1) == 1 else 0 for j in range(n)] for i in range(n)]
for linie in mat:
    print(*linie)