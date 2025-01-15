from itertools import*
k=0
comb = product('акру', repeat=5)
for i in comb:
    words = ''.join(i)
    k+=1
    print(k, words)