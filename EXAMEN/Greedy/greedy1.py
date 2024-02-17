L=[int(x) for x in input().split()]
C=[x for x in input().split()]
cuburi={}
for i in range(0,len(L)):
    cuburi[L[i]]=[i,C[i]]
print(cuburi)

L.sort(reverse=True)
print(L)
ordine=[cuburi[L[0]][0]]
for i in range(1,len(L)):
    if cuburi[L[i-1]][1]!=cuburi[L[i]][1]:
        ordine.append(cuburi[L[i]][0])
print(ordine)