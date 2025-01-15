from itertools import *
k = 0
for w in product('офчюя', repeat=5):
    words = ''.join(w)
    k += 1
    if ('оо' not in words) and ('ф' not in words ):
        print(k, words)
