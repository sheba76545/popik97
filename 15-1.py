def F(x, y, A):
    return (36 != y + 2*x) or (8* x > A) or (2 * y > A)

for A in range(160):
    if all(F(x, y, A) for x in range(160) for y in range(80)):
        print(A)