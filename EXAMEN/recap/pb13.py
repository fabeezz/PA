sir="Ana are mere si mai are si pere Are de asemenea si banane"
sir=sir.lower().split()
d={cuv : sir.count(cuv) for cuv in sir}

cuvinte=[cuv for cuv in d.keys() if d[cuv]==max(d.values())]

print(cuvinte)