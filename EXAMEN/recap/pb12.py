#unim dictionare
D1 = {'a':1, 'b':2, 'c':2}
D2 = {'b' :-1, 'c':2,'d':3}
d={x : D1.get(x,0) + D2.get(x,0) for x in D1.keys() or D2.keys()}
print(d)
