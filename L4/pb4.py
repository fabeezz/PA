with open("nume.in") as f:
    L=[]
    for linie in f:
        L.append(linie.split())
def pwd_gen():
    import secrets
    import string
    letters=string.ascii_letters
    digits=string.digits
    pwd=''
    pwd+=secrets.choice(letters).upper()
    for i in range(3):
        pwd+=secrets.choice(letters).lower()
    for i in range(4):
        pwd+=secrets.choice(digits)
    return pwd
out=[f"{L[k][1].lower()}.{L[k][0].lower()}@s.unibuc.ro - {pwd_gen()}" for k in range(len(L))]
with open("studenti.out", "w") as g:
    g.writelines("\n".join(out))