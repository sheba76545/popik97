from itertools import*
k = 0
for w in product('приказ', repeat=4):
    words = ''.join(w)
    if ((words.count('и')+words.count('а')) <= 1) and (words.count('п') <= 1) and (words.count('р') <= 1) and (words.count('к') <= 1) and (words.count('з') <=
                                                                                                                                           1):
        k += 1
        print(k, words)
