# COMBINARI

def bkt(k):
    global sol, n, m
    for v in range(1,n+1):
        sol[k]=v
        if k<=m and sol[k]>sol[k-1]:
            if k==m:
                print(*sol[1:])
            else:
                bkt(k+1)
n=int(input("n= "))
m=int(input("m= "))
sol=[0]*(m+1)
bkt(1)