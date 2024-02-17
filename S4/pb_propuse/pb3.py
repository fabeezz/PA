with open("carti.in") as f:
    C={}
    for l in f:
        linie=l.split()
        C[linie[0]]={'autori':linie[-(len(linie)+1):-2],'an':linie[-2],'pret':linie[-1]}
print(C)

def sale(C,percentage):
    for cheie in C:
        if int(C[cheie][-2])<2000:
            C[cheie][-1]=str(int(C[cheie][-1])*((100-percentage)/100))
#sale(C,20)
#print(C)

def yd_na(C):
    C=sorted(C, key=lambda x:(-x['an'], x))
yd_na(C)
print(C)
