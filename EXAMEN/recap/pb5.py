sir="Ana are mere? Tata are prune! Bunicu face tuica."
sir=sir.replace("!",".")
sir=sir.replace("?",".")
print(f"Sirul este alcatuit din {len(sir.split('.'))-1} propozitii. Cel mai lung cuvant are {max([len(element.strip()) for element in sir.split('.')])}")