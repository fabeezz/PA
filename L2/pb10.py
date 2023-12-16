cuv1=input("Cuv1:")
cuv2=input("Cuv2:")
if len(cuv1)!=len(cuv2):
    print("NU")
else:
    for l in cuv1:
        if cuv1.count(l)!=cuv2.count(l):
            print("NU")
            break
    else:
        print("DA")