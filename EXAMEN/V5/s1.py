def aparitii(*numbers):
    d={}
    for number in numbers:
        lista_cifre=[]
        lista_cifre_unice=[]
        for cifra in str(number):
            lista_cifre.append(int(cifra))
        for cifra in str(number):
            if int(cifra) not in lista_cifre_unice:
                lista_cifre_unice.append(int(cifra))
        d[number]=[]
        for cifra in lista_cifre_unice:
            if lista_cifre.count(cifra)>0:
                d[number].append((cifra,lista_cifre.count(cifra)))
    return d

d=aparitii(1011, 234, 8158558)
print(d)

L=[x for x in d.keys() if len(d[x])>=3]
print(L)