with open("elevi.in") as f:
    D={}
    for linie in f:
        L=linie.split()
        D[int(L[0])]=[L[1],L[2],[int(x) for x in L[3:]]]

def fb(cnp, dict_elevi):
    try:
        if dict_elevi[cnp][2][0]<10:
            dict_elevi[cnp][2][0]+=1
        return dict_elevi[cnp][2][0]
    except:
        return None
#cnp=1412900000041
#print(fb(cnp,D))

def fc(cnp, l_note, dict_elevi):
    try:
        dict_elevi[cnp][2].extend(l_note)
        return dict_elevi[cnp]
    except:
        return None
#l_note=[10,8]
#cnp=1412900000041
#print(cnp,*fc(cnp, l_note, D))

def fd(cnp, dict_elevi):
    try:
        dict_elevi.pop(cnp)
    except:
        pass
#cnp=1412900000041
#fd(cnp, D)
#print(D)

def fe(dict_elevi):
    out=[]
    for elem in dict_elevi.values():
        out.append(elem)
    def medie(lista_note):
        nr_note=len(lista_note)
        suma_note=0
        for note in lista_note:
            suma_note+=int(note)
        medie=suma_note/nr_note
        return medie
    for i in range(len(out)-1):
        for j in range(1,len(out)):
            if medie(out[i][2])<medie(out[j][2]):
                out[i],out[j]=out[j],out[i]
            elif medie(out[i][2])==medie(out[j][2]):
                if out[i][0]<out[j][0]:
                    out[i],out[j]=out[j],out[i]  
    return out
#print(fe(D))

def ff(dict_elevi):
    def code_gen():
        import secrets
        import string
        letters=string.ascii_letters
        digits=string.digits
        cod=''
        for i in range(3):
            cod+=secrets.choice(letters)
        for i in range(3):
            cod+=secrets.choice(digits)
        return cod
    for elev in dict_elevi:
        dict_elevi[elev].append(code_gen())
ff(D)
print(D)
    
