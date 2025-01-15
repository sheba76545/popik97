from itertools import product
k = 0
for w in product('01', repeat=5):
    words = ''.join(w)
    if (words.count('1') + 1) <= words.count('0'):
        k += 1
        print(k, words)
