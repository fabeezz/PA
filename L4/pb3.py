rezultat=[]
nota=1
with open("test.in") as f:
    for linie in f:
        A, rez=linie.split("=")
        x,y=A.split("*")
        if int(x)*int(y)==int(rez):
            rezultat.append(f"{linie} Corect")
            nota+=1
        else:
            rezultat.append(f"{linie} Gresit {int(x)*int(y)}")
    rezultat.append(f"Nota {nota}")
with open("test.out", "w") as g:
    g.write("\n".join(rezultat))