#punctul a)

s=input("sir:")
rez=""
nr=0
for i in range(len(s)):
    if s[i].isdigit():
        nr=nr*10+int(s[i])
    else:
        rez+=s[i]*nr
        nr=0
print(rez)

#punctul b)

