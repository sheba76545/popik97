from itertools import *
k = 0
s = set()
for w in permutations('каделак'):
    words = ''.join(w)
    if ('кк' not in words) and ('аа' not in words):
        s.add(words)
        print(len(s))











from itertools import permutations

count = set()

for x in permutations('каделак'):
    s = ''.join(x)
    if 'аа' not in s and 'кк' not in s:
        count.add(s)
print(len(count))