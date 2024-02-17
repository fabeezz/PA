def bkt(k):
    global sol, n, suma
    for v in range(1,n+1):
        sol[k]=v
        suma+=v
        if suma<=n and sol[k]>=sol[k-1]: # toate cond mai putin aia de sol completa
            if suma==n: # pot afisa solu
                print(sol)
            else:
                bkt(k+1)
        sol[k]=0
        suma-=v

n=int(input("n: "))
suma=0
sol=[0]*n
bkt(0)