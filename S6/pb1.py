# n=5 - nr siruri
# 20,10,25,15,20 -> lungimi de siruri
#  30, 25,15,20
#    55, 15, 20
#      70,  20
#        90
# Total=30+55+70+90 = 245

#                 20,10,25,15,20
# facem 10 cu 15: 20,25,25,20
# facem 20 cu 20: 40,25,25
# facem 25 cu 25: 40,50
# 90
# Total=25+40+50+90 = 205 < 245!

# PRIORITY QUEUE:
# inserare valoare, extragere minim/maxim --- ambele se realizeaza cu O(log2n)
# Python - clasa PriorityQueue (de tip minim) - import queue
#       (prioritate, valoare)
# Metode:
# 1) PriorityQueue()
# 2) put(elem)
# 3) get() - elem cu prioritate minima
# 4) qsize()

from queue import PriorityQueue
L=[int(x) for x in input("Lista lungimi: ").split()]
Q=PriorityQueue()
for elem in L:
    Q.put(elem)
total=0
while Q.qsize()>=2:
    R=Q.get()+Q.get()
    total+=R
    Q.put(R)
print(total)