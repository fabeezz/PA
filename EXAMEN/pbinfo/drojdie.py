def drojdie(k):
    global sol
    if k==0:
        return True
    else:
        for index in range(1,k+1):
            if abs(sol[index]-sol[index-1])!=1:
                return False
    return True
def bkt(k):
    global sol, A, B, afis
    for v in range(0,10):
        sol[k]=v
        if drojdie(k):
            p=1
            nr=0
            for cifra in sol :
                if cifra!=-1:
                    nr=nr+p*cifra
                    p=p*10
            if A<=nr and nr<=B:
                afis.append(nr)
                print(sol)
            else:
                bkt(k+1)
        sol[k]=-1

A=int(input())
B=int(input())
sol=[-1]*10
afis=[]
bkt(0)
afis.sort()
print(afis)

