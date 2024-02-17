def valid(lista, index, k):
    for i in range(1, index):
        if abs(lista[i] - lista[index]) > k:
            return False
    return True

def bkt(x):
    global s, G, n, k
    for v in range(1, G + 1):
        s[x] = v
        if valid(s, x, k):
            if x == n:
                if sum(s) == G:
                    print(*s[1:])
            else:
                bkt(x + 1)

G = int(input("G= "))
n = int(input("n= "))
k = int(input("k= "))

s = [0] * (n + 1)
bkt(1)
