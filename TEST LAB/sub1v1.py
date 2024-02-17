def citire_liste(nume_fisier):
    with open(nume_fisier) as file:
        m=int(file.readline())
        matrice=[[0 for i in range(m)] for j in range(m)]
        indexL=0
        indexC=0
        for line in file:
            line=line.split()
            valoare=int(line[0])
            nr_ori=int(line[1])
            for i in range(nr_ori):
                matrice[indexL][indexC]=valoare
                indexC+=1
                if indexC==m:
                    indexL+=1
                    indexC=0
    return matrice
L=citire_liste("liste.in")

def prelucrare_liste(L,x):
    L_noua=[]
    for sublista in L:
        sublista_noua=[]
        for index in range(len(sublista)):
            if index!=x:
                sublista_noua.append(sublista[index])
        if len(set(sublista_noua))!=1:
            L_noua.append(sublista_noua)
    return L_noua

LC=prelucrare_liste(L,2)
for lista in LC:
    print(*lista)

k=int(input("nr k= "))
ok=0
with open("multipli.out", "w") as output_file:
    lista_out=set()
    for lista in L:
        for numar in lista:
            if numar%k==0 and numar%(k**2)!=0:
                lista_out.add(numar)
                ok+=1
    if ok==0:
        output_file.write("Imposibil!")
    else:
        lista_out=sorted(lista_out, reverse=True)
        for numar in lista_out:
            output_file.write(str(numar)+'\n')