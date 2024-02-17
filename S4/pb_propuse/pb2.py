def check(colectie, cond):
    pozitii=[]
    for i in range(len(colectie)):
        if cond(colectie[i])==True:
            pozitii.append(i)
    return pozitii

def ng0(nr):
    if nr>0:
        return True
    else:
        return False
#L=(1,2,4,13,-12,-1,4,3,1)
#print(check(L,ng0))

def ispm(t):
    import string
    pm=string.punctuation
    if t in pm:
        return True
    else:
        return False
#sir="a,.a!"
#print(check(sir,ispm))

def anagram(cuv):
    if sorted(s)==sorted(cuv):
        return True
    else:
        return False
#L=["amari", "caine", "ramai"]
#s=input("Anagram tester: ")
#print(check(L,anagram))

def x_cond(nr):
    sum=0
    for digit in str(nr):
        sum+=int(digit)
    nrd=len(str(nr))
    if sum==s and nrd==n:
        return True
    else:
        return False
#n=int(input("How many digits: "))
#s=int(input("Sum of digits:"))
#L=[123,11111,212,5]
#print(check(L,x_cond))