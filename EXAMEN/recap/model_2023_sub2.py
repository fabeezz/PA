l=[[x.strip() for x in y.split("%")] for y in open("cinema.in","r").readlines()]

print(l)

for x in l:
    x[2]=x[2].split()
#print(l)

d={x[0] : {y[1] : set() for y in l if x[0]==y[0]} for x in l}

for x in l:
    d[x[0]][x[1]] |= set(x[2])

#print(d)

def sterge_ore(d, cinema, film, ore):
    d[cinema][film] -= ore
    return d[cinema]

cinema="Cinema 1"
film="Minionii 2"
ora=set(["12:30"])
sterge_ore(d, cinema, film, ora)

#print(d)