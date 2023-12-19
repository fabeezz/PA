def frecv(*numeFisiere):
    D={}
    for nume in numeFisiere:
        with open(nume) as f:
            L_cuv=f.read().split()
            for cuvant in L_cuv:
                #if cuvant not in D:
                    #D[cuvant]=1
                #else:
                    #D[cuvant]+=1
                D[cuvant]=D.get(cuvant,0)+1 #alternativa pt mai sus
    return D
#print(frecv("cuvinte1.in"))

D12=frecv("cuvinte1.in", "cuvinte2.in")
#C
D1=frecv("cuvinte1.in")
L=sorted(D1.items(), key=lambda t:t[1], reverse=True)
print(L)

#D
D2=frecv("cuvinte2.in")
print(D2)
print(max(sorted(D2.items(), key=lambda t:t[0]), key=lambda t:t[1]))

#E
S12=sum(D1.get(cuvant,0)*D2.get(cuvant,0) for cuvant in D12)
N1=sum(val**2 for val in D1.values())**0.5
N2=sum(val**2 for val in D2.values())**0.5
res=S12/(N1*N2)
print(round(res,2))
