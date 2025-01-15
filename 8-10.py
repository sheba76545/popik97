from itertools import product
k = 0
for w in product('авикнст', repeat=4):
    words = ''.join(w)
    if (w[3] == 'а' or w[3] == 'и') and (w[0] == 'в' or w[0] == 'к' or w[0] == 'н' or w[0] == 'с' or w[0] == 'т'):
        k += 1
        print(k, words)
