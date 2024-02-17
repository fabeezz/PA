def bkt(k):
    global sol, multime, rez
    for v in multime:
        sol[k]=v
        if sol[k] not in sol[:k]:
            if k<=len(multime)+1:
                print(sol[1:])
            else:
                bkt(k+1)
        sol[k]=0

multime=[int(x) for x in input("Multime: ").split()]
sol=[0]*(len(multime)+1)
bkt(1)
