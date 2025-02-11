k = 0

p = 0

for i in range(1,10):

    if (B[i] > B[p]  and  B[i] % 2 == 0):

    k += i

    t = B[i]

    B[i] = B[p]

    B[p] = t
print(k)