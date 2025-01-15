from itertools import *
k = 0
for w in product('0123456789ABCDE', repeat=5):
    words = ''.join(w)
    if (words[0] != '0') and (words.count('8') == 1) and (words.count('A')+words.count('B')+words.count('C')+words.count('D')+words.count('E') >= 2):
        k += 1
        print(words, k)
