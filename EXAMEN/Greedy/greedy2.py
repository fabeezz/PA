'''
N=int(input("Nr. bancnote: "))s
bancnote=[int(x) for x in input("Bancnote in ord. crescatoare: ").split()]
S=int(input("Suma: "))
'''
def min_bancnote_greedy(N, S, B):
    B.sort(reverse=True)
    count = 0
    for i in range(N):
        count += S // B[i]
        S %= B[i]
    return count if S == 0 else -1

print(min_bancnote_greedy(7,130,[1 ,2 ,4 ,12 ,24 ,25 ,30]))