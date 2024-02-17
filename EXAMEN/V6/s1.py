def palindrom(*cuvinte):
    d={}
    for cuvant in cuvinte:
        if cuvant==cuvant[::-1]:
            nr_voc=0
            for vocala in "aeiou":
                nr_voc+=cuvant.count(vocala)
            print(nr_voc, cuvant)
            if nr_voc>len(cuvant)-nr_voc:
                d[cuvant]=list(set([vocala for vocala in cuvant if vocala in "aeiou"]))
            else:
                d[cuvant]=list(set([consoana for consoana in cuvant if consoana not in "aeiou"]))
    return d
#print(palindrom('asa','merem','palindrom'))

L=[x for x in range(10,100) if (x%7!=0 and x**0.5!=int(x**0.5))]
print(L)

