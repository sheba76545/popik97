k=0
from itertools import product
for p in product('012345678',repeat=5):
    s=''.join(p)
    if ((s.count('0') ==1) and  (not('01' in s or '03' in s or '05' in s or '07' in s or '10' in s or '30' in s or '50' in s or '70' in s))):
        k+=1
        print(s,k)
