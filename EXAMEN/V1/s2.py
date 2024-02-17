nrl=int(input("Nr. linii: "))
nrc=int(input("Nr. coloane: "))
biju=[]
for i in range(nrl):
    lista=[float(x) for x in input().split()]
    biju.append(lista)
print(biju)
pozitii=[]
val=min(biju[0])
suma=val
pozitii=[(1,biju[0].index(val))+1]
for i in range(1,nrl):
    for j in range(nrc):
        if biju[i][j]>=val: #.............
            
print(suma, pozitii)