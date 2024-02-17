sir="PI=3.141526 si e=2.718123"
cifre = "0123456789"
r = sir.split(".")
for i in range(len(r)):
    if i==0:
        r[i] = r[i].rstrip(cifre)
    elif i==len(r)-1:
        r[i] = r[i].lstrip(cifre)
    else:
        r[i] = r[i].strip(cifre)
print("".join(r))