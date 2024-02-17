def bkt(k):
    global s,p
    for v in range(s[k-1],p//2+1):
        s[k]=v
        if s[k]>=s[k-1]:
            if sum(s)<=p:
                if sum(s)==p:
                    print(*s[1:])
                else:
                    s[k]=0
                
p=int(input("Lungimea: "))
s=[0]*(p+1)

bkt(1)