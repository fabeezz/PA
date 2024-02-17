def modifica_prefix(x, y, prop):
    nr_modificari = 0
    propozitie_noua = []
    propozitie = prop.split()
    lungime_cuvant = len(x)

    for cuvant in propozitie:
        if cuvant[:len(x)] == x:
            cuvant_nou = y + cuvant[len(x):]
            nr_modificari += 1
            propozitie_noua.append(cuvant_nou)
        else:
            propozitie_noua.append(cuvant)

    prop_noua = " ".join(propozitie_noua)
    prop=prop_noua
    return prop, nr_modificari

x = "apa"
y = "mama"
prop = "andrei are un aparat tare aparatura noua"
#print(modifica_prefix(x, y, prop))

def poz_max(lista_nr):
    val_max=max(lista_nr)
    poz_val_max=[]
    for i in range(len(lista_nr)):
        if lista_nr[i]==val_max:
            poz_val_max.append(i+1)
    return poz_val_max
#print(*poz_max([1,5,4,3,1,5,2]))

inlocuit=input("ce inlocuim? ")
incoluitorul=input("cu ce inlocuim? ")

with open("propozitii.in") as f:
    vector_modif=[]
    g=open("propozitii_modificate.out", "w")
    for line in f:
        nr_modif_linie=modifica_prefix(inlocuit,incoluitorul,line)[1]
        vector_modif.append(nr_modif_linie)
        prop_modificata=modifica_prefix(inlocuit,incoluitorul,line)[0]
        g.write(prop_modificata)
        g.write("\n")
    print(*poz_max(vector_modif))