def bkt(k):
    global sol, L, S, n, ok
    if T[k]=="l":
        for litera in L:
            sol[k]=litera
            if sol[k] not in sol[:k]:   #solutie partiala (toate cond mai putin aia de final)
                if k==len(T)-1:  # solutie finala (cond de final)
                    ok=1
                    if sol[0] in "aeiouAEIOU":
                        print(sol)
                else:
                    bkt(k+1)
            sol[k]=0
    else:
        for simbol in S:
            sol[k]=simbol
            if sol[k] not in sol[:k]:
                if k==len(T)-1:
                    ok=1
                    if sol[0] in "aeiouAEIOU":
                        print(sol)
                else:
                    bkt(k+1)
            sol[k]=0
            
ok=0
n=int(input("n: "))
T=input("T: ")
L=[l for l in input("Litere:").split()]
S=[l for l in input("Simboluri:").split()]
sol=[0]*n
bkt(0)
