nume=input("nume:")
sir=nume.split()
n=len(sir)
if n>2:
    print("Nu este un nume complet corect")
else:
    for s in sir:
        if s.count("-")>1:
            print("Nu este un nume corect")
            break
        else:
            if s[0].isupper()==0:
                print("Nu este un nume corect")
                break
            for lit in s:
                if lit.isalpha()==0:
                    print("Nu este un nume corect")
                    break
                