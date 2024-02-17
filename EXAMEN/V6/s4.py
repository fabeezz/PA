def diferenta(lista,index,p):
    for i in range(1,index):
        if abs(lista[i] - lista[index]) > p:
            return False
    return True
def bkt(k):
    global s,p,c,suma
    for x in range(1,10):
        s[k]=x
        suma+=x
        if suma<=c:
            if suma==c:
                if diferenta(s,k,p):
                    print(*s)
            else:
                bkt(k+1)
        s[k]=0
        suma-=x

p=int(input("p= "))
c=int(input("c= "))
s=[0]*c
suma=0
bkt(0)