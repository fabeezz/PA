def divizori(*numbers):
    def prim(x):
        for divizor in range(2,int(x**0.5)+1):
            if x % divizor == 0:
                return False
        if x>1:
            return True
    d={}
    for number in numbers:
        if number==0 or number==1:
            d[number]="esti obraznic"
        d[number]=[x for x in range(2,number//2) if prim(x)==True and number%x==0]
    return d
print(divizori(1,50,21))

litere_10=[chr(lit) for lit in range(ord('a'),ord('j')+1)]
print(litere_10)

