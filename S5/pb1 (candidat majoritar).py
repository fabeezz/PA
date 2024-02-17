# v=[1,5,3,5,3,5] => nu exista castigator
# v=[5,5,3,5,1,5] => castigator=5

# solutia 1 - O(n^2)

def castigator(voturi):
    for v in set(voturi):
        if voturi.count(v)>len(voturi)//2:
            return v
    return None

voturi=[5,5,3,5,1,5]
print(castigator(voturi))

# solutia 2 - O(nlogn)

def castigator2(voturi):
    voturi.sort()
    poz=len(voturi)//2
    if voturi.count(voturi[poz])>poz:
        return voturi[poz]
    else:
        return None
print(castigator2(voturi))

# solutia 3 - O(n)

def castigator3(voturi):
    d={}
    for candidat in voturi:
        if candidat not in d:
            d[candidat]=1;
        else:
            d[candidat]+=1;
    for vot in d:
        if d[vot] > len(voturi)//2:
            return vot
    return None
print(castigator3(voturi))

# solutie 4 - O(n) ALG. BOYER-MOORE

votes=[5,5,1,2,1,1,1,5,1,7,1]
#candmaj=None,5,5,5,5,1,1,1,1,1,1,1
#avantaj=0,   1,2,1,0,1,2,3,2,3,2,3 > 0

def castigator4(voturi):
    cmaj=None
    avantaj=0
    for candidat in voturi:
        if avantaj==0:
            cmaj=candidat
            avantaj=1
        else:
            if candidat!=cmaj:
                avantaj-=1
            else:
                avantaj+=1
    if avantaj==0:
        return None
    elif voturi.count(cmaj)>len(voturi)//2:
        return cmaj
    else:
        return None

print(castigator4(votes))      


