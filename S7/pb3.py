# (x,y) x<y
# (x1,y1), ... ,(xi,yi),(xi+1,yi+1), ... (xk,yk) a.i. yi<xi+1, i din {1,2,...,k-1}
# ex: n=6
# (12,15), (6,8), (5,7), (20,30), (9,11), (13,18)
# lmax=4 pt. (5,7), (9,11), (12,15), (20,30)
# (12,15), (6,8), (5,7), (20,30), (9,11), (13,18)
#      (5,7), (6,8), (9,11), (12,15), (13,18), (20,30) - (sortat dupa y)
# lmax   4      4      3        2        2        1
# succ   2      2      3        5        5        1

with open("perechi.txt") as f:
    lista_perechi=[]
    for line in f:
        pereche=tuple(int(x) for x in line.split())
        lista_perechi.append(pereche)
lista_perechi.sort(key=lambda x:x[1])
n=len(lista_perechi)
lmax=[1 for i in range(n)]
succ=[-1 for i in range(n)]
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if lista_perechi[j][0]>lista_perechi[i][1] and 1+lmax[j]>lmax[i]:
            lmax[i]=1+lmax[j]
            succ[i]=j
lungime_maxima=max(lmax)
print(lungime_maxima)