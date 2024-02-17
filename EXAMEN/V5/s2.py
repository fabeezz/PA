n=int(input("Nr. de participanti: "))
n+=1
valori=[int(x) for x in input("Valoari: ").split()]
valori.sort()
castig=0
for om in valori:
    castig+=om/n
    n-=1
print(round(castig,3))

