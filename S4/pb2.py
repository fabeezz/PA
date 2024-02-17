def cauta(x,*liste):
    R=[]
    for lista in liste:
        if x in lista:
            R+=[lista]
    return R
