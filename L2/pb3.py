s=input("s=")
for i in range(len(s)//2+1):
    print(s[i:len(s)-i].center(len(s)))