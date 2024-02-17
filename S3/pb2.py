#L=[[2,1,5,1,3],[1,4,2,2],[2,1,1,6,8]] # 1,2 (elementele comune)
n=int(input("Numarul de linii:"))
L=[]
for i in range(n):
    aux=[int(x) for x in input().split()]
    L.append(aux)
M=set(L[0])
for i in range(1,n):
    M=M&set(L[i])
print(M)

