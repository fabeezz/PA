def citire_numere(nume_fisier):
    with open(nume_fisier) as f:
        lista=[]
        for linie in f:
            lista.append([int(elem) for elem in linie.split()])
    return lista
lista_numere=citire_numere("numere.in")

def prelucrare_lista(lista):
    len_sublista=9999 #not optimal
    for sublista in lista:
        minim=min(sublista)
        while minim in sublista:
            sublista.remove(minim)
        if len(sublista)<len_sublista:
            len_sublista=len(sublista)
    for sublista in lista:
        i=len(sublista)-len_sublista
        while i>0:
            sublista.pop()
            i-=1
#prelucrare_lista(lista_numere)
print(lista_numere)
#for linie in lista_numere:
    #print(*linie)
k=int(input("Numarul de cifre: "))
lista_k=[]
for linie in lista_numere:
    for elem in linie:
        if len(str(elem))==k:
            if str(elem) not in lista_k:
                lista_k.append(str(elem))
if lista_k!=[]:
    lista_k.sort(reverse=True)
    with open("numere.out", "w") as g:
        g.write(" ".join(lista_k))
else:
    with open("numere.out", "w") as g:
        g.write("Imposibil")

