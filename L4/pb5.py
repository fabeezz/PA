def negative_positive(L):
    LN=[]
    LP=[]
    for nr in L:
        if nr<0:
            LN.append(nr)
        else:
            LP.append(nr)
    Lf=[]
    Lf.extend(LN)
    Lf.extend(LP)
    return Lf
L=[1,-2,5,6,7,-2,-12,5]
fin=[]
for elem in negative_positive(L):
    fin.append(str(elem))
print(fin)
with open("date.out", "w") as g:
    g.writelines(" ".join(fin))