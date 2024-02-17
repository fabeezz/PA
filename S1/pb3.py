x=int(input("x="))
y=int(input("y="))
t=x^y
i=0
while t!=0:
    if t&1==1:
        i=i+1
    t=t>>1
print(i)