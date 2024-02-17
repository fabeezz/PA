tt_cinema={}
with open("cinema.in") as f:
    for linie in f:
        linieD=linie.strip().split('%')
        linieFix=[]
        for elem in linieD:
            linieFix.append(elem.strip())
        rest=linieFix[2].split()
        entry={linieFix[1] : rest}
        if linieFix[0] not in tt_cinema:
            tt_cinema[linieFix[0]]=[entry]
        else:
            tt_cinema[linieFix[0]].append(entry)
print(tt_cinema)
print(tt_cinema['Cinema 1'][1]['Minionii 2'])
def sterge_ore(tt_cinema, cinema, film, ore):
    tt_cinema[cinema][film]