sir=input("sir=")
s=input("cuv de inlocuit:")
t=input("cuv cu care inlocuim:")
x=sir.split()
#for i in x:
#    if i==s:         GRESIT
#        i=t
for i in range(len(x)):
    if x[i]==s:
        x[i]=t
s2=" ".join(x)
print(s2)