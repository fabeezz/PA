#VARIANTA_1 - O(n^2)
lista=[int(x) for x in input("Sir:").split()]
n=len(lista)+1
for i in range(1,n+1):
    if i not in lista: # in si not in au complexitate O(n)
        print()
        break

#VARIANTA_2
lista=[int(x) for x in input("Sir:").split()]
lista.sort()
n=len(lista)+1
for x in range(1,n):
    st=0
    dr=n-2
    while st<=dr:
        mij=(st+dr)//2
        if lista[mij]==x:
            break
        if x>lista[mij]:
            st=mij+1
        else:
            dr=mij-1
    else:
        print(x)
        break

#VARIANTA_3 - O(nlog2(n))
L=[int(x) for x in input("LISTA ESTE:").split()]
L.sort()
if L[len(L)-1]==len(L):
    print(len(L)+1)
else:
        for x in range(len(L)):
            if L[x]!=x+1:
                print(x+1)
                break

#VARIANTA_4 - O(n)
lista=[int(x) for x in input("Sir:").split()]
suma=sum(lista)
n=len(lista)+1
st=n*(n+1)/2

#VARIANTA_5 - O(n)
lista=[int(x) for x in input("Sir:").split()]
x=0
for i in range(len(L)):
    x=x^(i+1)^L[i]
x=x^(i+1)
print(x)

#VARIANTA_6 - O(n)
sir1={int(x) for x in input("Sir:").split()}
n=len(sir1)+1
sir2={x+1 for x in range(n)}
dif=sir2-sir1
print(dif)

#VARIANTA_7 - DICTIONARE
lista=[int(x) for x in input("Sir:").split()]
n=len(lista)+1
M={x:False for x in range(1,n+1)}
for x in L:
    M[x]=True
for x in range(1,n+1):
    if M[x]==False:
        print(x)
        break