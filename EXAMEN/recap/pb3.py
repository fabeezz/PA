with open("poezie.txt") as f:
    for line in f:
        print(line[:len(line)-1].center(50))