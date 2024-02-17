def citire_cuvinte(nume_fisier):
    with open(nume_fisier) as f:
        n=int(f.readline())
        cuvinte=f.read().strip().split()
        ll=[[] for q in range (n)]
        for i in range(1,len(cuvinte)+1):
            if i%n==0:
                ll[n-1].append(cuvinte[i-1])
            else:
                ll[i%n-1].append(cuvinte[i-1])
        return ll
ll=citire_cuvinte("cuvinte.in")

def prelucrare_cuvinte(L,w,x):
    # w = cuvant
    # x = litera
    L_new=[]
    for lista in L:
        lista_new=[]
        ok=1
        for index_cuv in range(len(lista)):
            cuv_nou=lista[index_cuv]
            if lista[index_cuv][-len(w):]==w:
                cuv_nou=lista[index_cuv][:len(lista[index_cuv])-len(w)]+x
            lista_new.append(cuv_nou)
        for index_cuv in range(len(lista_new)):
            if lista_new[index_cuv][::-1]==lista_new[index_cuv]:
                ok=0
        if ok!=0:
            L_new.append(lista_new)
    return L_new

lista_afis=prelucrare_cuvinte(ll,"re","u")
#print(*lista_afis[0])

print(ll)

w=input("cuvant: ")
with open("cuvinte.out","w") as g:
    lista_cuv=set()
    ok=0
    for lista in ll:
        for cuv in lista:
            if len(cuv)<=len(w):
                ok=1
                lista_cuv.add(cuv)
    lista_cuv=sorted(lista_cuv)
    for cuvant in lista_cuv:
        g.write(cuvant)
        g.write('\n')
    #if ok!=0:





