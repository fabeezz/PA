# O(nlog2n + n*zi_max) => O(n*zi_max)

with open("proiecte.in") as f:
    proiecte=[]
    for line in f:
        aux=line.split()
        proiecte.append((aux[0],int(aux[1]),float(aux[2])))
proiecte.sort(key=lambda x:x[2], reverse=True)
print(proiecte)

zi_max=max([x[1] for x in proiecte])
solutie={zi:None for zi in range(1, zi_max+1)}

profit_total=0
for x in proiecte:
    for i in range(x[1], 0, -1):
        if solutie[i] is None:
            solutie[i]=x
            break
profit_total=sum([solutie[x][2] for x in solutie if solutie[x] is not None])
with open("proiecte.out", "w") as g:
    g.write(f"Profit maxim: {profit_total}\n")
    for k in solutie:
        if solutie[k] is not None:
            g.write(f'Ziua {k}: {solutie[k][0]} {solutie[k][2]}\n')

        