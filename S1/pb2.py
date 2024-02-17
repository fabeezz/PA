n=int(input("Nr. de elemente:"))
v=[]
rez=0
for i in range(0,n):
    x=int(input("Element:"))
    v.append(x)
nr=(2**(n-1))
if nr%2==0:
    print(0)
else:
    while n>=0:
        rez=rez^v[n]
        n=n-1
    print(rez)
