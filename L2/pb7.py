sir=input("jurnal:")
x=sir.split()
nr=0
for cuv in x:
    if cuv.isdigit():
        nr+=int(cuv)
print(f"{nr} RON")