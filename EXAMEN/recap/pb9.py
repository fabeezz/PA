def is_prime(x):
    if x<=1:
        return False
    d=2
    while d*d <= x:
        if x%d==0:
            return False
        d+=1
        return True

n=20
lista=[x for x in range(1,n+1) if is_prime(x)]
print(lista)