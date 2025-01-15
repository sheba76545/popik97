from itertools import *
k = 0
for w in product('012345678', repeat=5):
    integers = ''.join(w)
    if (integers[0] != '0') and (integers.count('0') == 1) and ('10' not in integers) and ('01' not in integers) and ('30' not in integers) and ('03' not in integers) and ('05' not in integers) and ('50' not in integers) and ('70' not in integers) and ('07' not in integers):
        k += 1
        print(k, integers)