s=input("Sirul:")
s=s.split()
tot=0
nr1=None
for cuv in s:
    try:
        aux=float(cuv)
        if nr1 is None:
            nr1=aux
        else:
            nr2=aux
            tot=tot+nr1*nr2
        nr1=None
    except:
        pass
print(f"Am cheltuit {tot}")