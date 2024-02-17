n=int(input("n= "))
g=float(input("g= "))
greutati=[]
for i in range(1,n+1):
    greutati.append((float(input()),i))
greutati.sort(key=lambda x:x[0])
sol=[]
cnt=0
st=0
dr=1
while st<=len(greutati)-1:
    if dr<=len(greutati)-1 and st!=dr:
        if abs(greutati[st][0]-greutati[dr][0])<=g:
            cnt+=1
            sol.append(f"{greutati[st][1]} + {greutati[dr][1]}")
            print(greutati)
            greutati=greutati[:st]+greutati[st+1:dr]+greutati[dr+1:]
            print(greutati)
            print(sol)
        else:
            st+=1
    else:
        break
print(cnt)
