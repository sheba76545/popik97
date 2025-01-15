from itertools import *
k = 0
for w in product('крот', repeat=6):
    words = ''.join(w)
    if words.count('о') == 1:
        k += 1
        print(k)