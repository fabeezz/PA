#PB6
n=int(input("nr:"))
c=9
maxi=0
while c>=0:
    copy=n
    while copy!=0:
        if(copy%10 == c):
            maxi=maxi*10+c
        copy//=10
    c=c-1
print(maxi)
mini=0
c=1
c0=0
copy=n
ok=0
while copy!=0:
    if copy%10==0:
        c0=c0+1
    copy//=10
while c<=9:
    copy=n
    while copy!=0:
        if copy%10==c:
            if ok==0:
                ok=1
                mini=mini*10+c
                mini=mini*(10**c0)
            else:
                mini = mini * 10 + c
        copy//=10
    c=c+1
print(mini)

#PB7
x=int(input("lungimea intiala a sariturii:"))
n=int(input("nr de sarituri dupa care apare p:"))
p=float(input("procentul:"))
m=int(input("nr sarituri:"))
p=(100-p)/100
dist=0
while m!=0:
    if m>=n:
        dist=dist+x*n
        x=x*p
        m=m-n
    else:
        dist=dist+x*m
        m=0
print(round(dist,2))