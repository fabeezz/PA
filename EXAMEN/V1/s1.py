def numere(*numbers):
    d={}
    numere=[]
    for nr in numbers:
        numere.append(nr)
    numere.sort(reverse=True)
    for nr in numere:
        medie=0
        for cifra in str(nr):
            medie+=int(cifra)/len(str(nr))
        if medie not in d:
            d[medie]=[nr]
        else:
            if nr not in d[medie]:
                d[medie].append(nr)
    print(d)
numere(82375, 201, 51, 73, 3456, 2855,  1021, 90, 153)

L=[x*100+y*10+z for x in range(1,10) for y in range(x+1,10) for z in range(y+1,10)]
print(L)