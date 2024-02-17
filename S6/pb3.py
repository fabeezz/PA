lsb=[0,0,0,0,1,1,1]
#            |
#          poz=4
def poz_1(L):
    def cb(l, st, dr):
        mij=(st+dr)//2
        if L[mij]==1:
            if L[mij-1]==0:
                return mij
            else:
                return cb(L,st,mij-1)
        else:
            return cb(L,mij+1,dr)
    if L[0]==1:
        return 0
    elif L[-1]==0:
        return -1
    else:
        cb(L,0,len(L)-1)

lista=[2,5,5,5,5,7,7,10,11,11]
x=5