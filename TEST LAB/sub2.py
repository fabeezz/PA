with open ("vacanta.in") as f:
    destinatie={}
    for line in f:
        line=line.split()
        if line[0]=="Destinatie:":
            locatie=line[1]
            destinatie[locatie]=[]
        else:
            if locatie in destinatie:
                destinatie[locatie].append([" ".join(line[:-3]), int(line[-3]), float(line[-1])])

def recomandari(dict, *nume_orase, nr_stele_min=0, scor_min=0):
    info_utile=[]
    lista_unitati_cazare=[]
    #dict=sorted(dict, key=lambda x:x[1], reverse=True)
    #print(dict)
    for nume_oras in nume_orase:
        for lista_cazari in dict[nume_oras]:
            if lista_cazari[1]>=nr_stele_min and lista_cazari[2]>=scor_min:
                lista_unitati_cazare.append(lista_cazari[0])
        info_utile.append((nume_oras,lista_unitati_cazare))
    return info_utile

print(recomandari(destinatie, "Sinaia", "Predeal"))