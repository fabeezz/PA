with open("text.in") as f:
    aparitii=[]
    text=f.read().lower()
    semne=".,!?:;"
    frecventa={}
    for semn in semne:
        text=text.replace(semn,"")
    text=text.strip().split()
    nr_caractere=0
    for cuvant in text:
        for caracter in cuvant:
            if caracter.isalpha()==True:
                nr_caractere+=1
    for cuvant in text:
        for litera in "abcdefghijklmnopqrstuvwxyz":
            for caracter in cuvant:
                if caracter==litera:
                    if litera not in frecventa:
                        frecventa[litera]=1/nr_caractere
                    else:
                        frecventa[litera]+=1/nr_caractere
    for key in frecventa:
        frecventa[key]=round(frecventa[key],3)
    aparitii=list(frecventa.items())
    aparitii.sort(key=lambda x:x[1], reverse=True)
with open("text.out", "w") as g:
    for tuplu in aparitii:
            g.write(str(tuplu[0])+": "+str(tuplu[1])+"\n")