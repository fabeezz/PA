L=[2,5,7,8,10,12,15,17,25]
s=20

# soluia 1 - O(n*k)

M=set(L)
for x in L:
    if s-x in M:
        
# solutie optima - O(n)
1) L[st]+L[dr]>S => dr-=1
2) L[st]+L[dr]<S => st+=1
3) L[st]+L[dr]=S => st+=1 si dr-=1