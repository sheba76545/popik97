def D(n, m):
    if n%m==0:
        return True
    else:
        return False

for A in range(1, 1000):
    k=0
    for x in range(1, 1001):
        if D(x, A) or (not(D(x, 16)) or not(D(x, 24))):
            k=k+1
    if k==1000:
        print(A)