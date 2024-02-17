def gen_strN(n,siruri):
    i=0
    while i<len(siruri):
        if len(siruri[i])==n:
            yield siruri[i]
        i+=1
siruri=["maria","ioana","andreea","carmen","alexa"]
for sir in gen_strN(5,siruri):
    print(sir, end=" ")
