def citire_matrice(nume_fisier):
    with open(nume_fisier) as f:
        matrice=[]
        len2=0
        ok=1
        for line in f:
            linie_matrice=line.strip().split()
            len1=len(linie_matrice)
            matrice.append(linie_matrice)
            if len2!=0:
                if len2!=len1:
                    ok=0
            len2=len1
    if ok==0:
        return None
    else:
        return matrice

#nume_fisier=input("Nume fisier: ")
matrix=citire_matrice("matrice.in")
"""
if matrix!=None:
    for linie in matrix:
        print(*linie)
else:
    print(None)
"""
def multimi(matrice, *n):
    reuniune=set()
    ok=0
    for index in n:
        neg=set()
        pegu=set()
        linia_index=matrice[index]
        if ok==0:
            intersectie = set(int(nr) for nr in matrice[index])
            ok=1
        for nr in linia_index:
            element=int(nr)
            if element<0:
                neg.add(element)
            else:
                elem_str=str(element)
                if elem_str[-1]==elem_str[0]:
                    pegu.add(element)
        intersectie=intersectie & neg
        reuniune=reuniune | pegu
    return intersectie, reuniune

print(*multimi(matrix,-1,-2,-3)[1])
print(len(multimi(matrix,0,-1)[0]))




