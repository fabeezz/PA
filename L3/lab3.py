#R=sorted(L,reverse=True,key=fct)
##A                
#la=[chr(x) for x in range(ord('a'),ord('z')+1)]               
#print(la)                 
#
##B                
#lb=[x*((-1)**x) for x in range(1,int(input("Pana la cat:"))+1)]               
#print(lb)                 
#
#lb1=[(x if x%2==1 else -x) for x in range(1,int(input("Pana la cat:"))+1)]                
#print(lb1)                
#
##C                
#l=[1,2,3,6,4,5,-11,-12]               
#lc=[x for x in l if x%2==1]               
#print(lc)                 
#
##D                
##ca la E                  
#
##E                
#le=[l[i] for i in range(len(l)) if l[i]%2==i%2]               

#F
#L=[1,2,3,4,5]
#lf=[(L[i],L[i+1]) for i in range(len(L)-1)]
#print(lf)

#G
#n=int(input("n="))
#lg=[[f"{x}*{y}={x*y}" for y in range(1,n+1)] for x in range(1,n+1)]
#for lin in lg:
    #print(*lin, sep="\t")

#H



#I
#n=int(input("numar:"))
#Li=[[x]*x for x in range(n)]
#print(Li)



#SORTARI
#b
#L=[1,4,7,45,2,1,564,123,54]
##print(sorted(L, key=lambda x:str(x)[::-1]))

#c
#print(sorted(L, key=lambda x:len(str(x)), reverse=True))
#print(sorted(L, key=lambda x:len(str(x))))

#d
#def cf(x):
    #nr=0
    #x=str(x)
    #for i in "0123456789":
        #if x.find(i)!=-1:
            #nr+=1
    #return nr
#L=[1,4,71234,45,241,1,56564,123243,5421]
#print(sorted(L, key=lambda x:cf(x)))

#e
#L=[1,4,7,45,2,1,564,123,54]
#print(sorted(sorted(L, key=lambda x:len(str(x)))))
#print(sorted(L, key=lambda x:len(str(x))))

