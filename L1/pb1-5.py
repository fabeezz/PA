#PB1
"""
x=int(input("x= "))
x1=x
inv=0
while x1!=0:
    inv=inv*10+x1%10
    x1=x1//10
if inv==x:
    print("palindrom")
else:
    print("nu e palindrom")
"""

#PB2
'''
n=int(input("nr zile:"))
ieri=float(input("val:"))
difmax=-1
while n!=1:
    azi=float(input("val:"))
    if azi>=ieri:
        dif=azi-ieri
    else:
        dif=ieri-azi
    if dif>difmax:
        difmax=dif
        ziua=n
    n-=1
print("Cresterea a fost de: ", round(difmax,2), "in ziua: ", ziua-1, " spre ", ziua)
'''

#PB3
'''
lungime=int(input("lungime:"))
latime=int(input("latime:"))
def cmmdc(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
latura=cmmdc(lungime,latime)
arie_mica=latura*latura
arie_mare=lungime*latime
nr_placi=arie_mare//arie_mica
print(nr_placi, "de placi de latura", latura)
'''

#PB4
'''
n=int(input("Nr numere:"))
max1=int(input())
max2=int(input())
n=n-2
while n!=0:
    nr=int(input())
    if nr>max1:
        max2=max1
        max1=nr
    n=n-1
if max1==max2:
    print("imposibil")
else:
    print(max1,max2)
'''
#PB5
'''
a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if d<0:
    print("nu are rad imaginara")
elif d==0:
    x1=(0-b)/(2*a)
    print(x1)
elif d>0:
    x1=((0-b)-(d**0.5))/(2*a)
    x2=((0-b)+(d**0.5))/(2*a)
    print(x1,x2)
'''