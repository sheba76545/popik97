from itertools import *
k = 0
for w in product('фокс', repeat=5):
    words = ''.join(w)
    if (words.count('ф')) == 1 or (words.count('ф') == 2):
        k += 1
        print(words, k)
        