def citire_matrice(nume_fisier):
    matrix=[]
    with open(nume_fisier) as input_file:
        for line in input_file:
            linie=[]
            line=line.split()
            for nr in line:
                linie.append(int(nr))
            matrix.append(linie)
    return matrix

matrix = citire_matrice("date.in")

def printare_matrix(matrix):
    for linie in matrix:
        print(*linie)

def fun(matrice, ch, x=0, y=0):
    if ch=="c":
        for linie in matrice:
            linie[x],linie[y]=linie[y],linie[x]
    elif ch=="d":
        for i in range(len(matrice)):
            matrice[i][i],matrice[i][len(matrice)-1-i]=matrice[i][len(matrice)-1-i],matrice[i][i]
    return matrice

for index in range(len(matrix)//2):
    fun(matrix, "c", index, len(matrix)-index-1)
fun(matrix, "d")

with open("date.out", "w") as g:
    ok=0
    for linie in matrix:
        if ok%2==0:
            for nr in linie:
                g.write(str(nr)+" ")
        else:
            linie=linie[::-1]
            for nr in linie:
                g.write(str(nr)+" ")
        ok+=1