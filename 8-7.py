from itertools import *
k = 0
for w in product('косф', repeat=4):
    words = ''.join(w)
    k += 1
    if 'фокс' in words:
        print(k, words)