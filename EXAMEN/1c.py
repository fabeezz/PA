def f(lista): 
    global cnt
    cnt+=1
    if len(lista) <= 2: 
        return sum(lista) 
    k = len(lista) // 3 
    aux_1 = lista[:k] 
    aux_2 = lista[k: 2*k] 
    aux_3 = lista[2*k:] 
    return f(aux_1) + f(aux_2) + f(aux_3) 

cnt=0
f([1,2,3,4,5,6,7,8,9])
print(cnt)
