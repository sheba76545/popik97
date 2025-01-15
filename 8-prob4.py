from itertools import product
k = 0
for w in product('01234567', repeat=5):
    words = ''.join(w)
    if words[0] != '0':
        if words.count('2') == 2:
            if '22' not in words:
                k += 1
                print(k, words)
