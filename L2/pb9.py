print(ord('A')) #A=65
print(ord('Z')) #Z=90
print(ord('a')) #a=97
print(ord('z')) #z=122
sir=input("Sir:") 
k=int(input("Pas:"))
n=len(sir)
sirnou=""
for i in range(n):
    if sir[i].isalpha()==True:
        if sir[i].isupper()==False:
            if ord(sir[i])+k<=122:
                sirnou+=chr(ord(sir[i])+k)
            else:
                sirnou+=chr(96+ord(sir[i])+k-122)
        else:
            if ord(sir[i])+k<=90:
                sirnou+=chr(ord(sir[i])+k)
            else:
                sirnou+=chr(64+ord(sir[i])+k-90)
    else:
        sirnou+=sir[i]
print(sirnou)