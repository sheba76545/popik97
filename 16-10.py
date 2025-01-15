def f(n):
    if n == 1:
        return 1
    if (n > 1) and (n % 2 == 0):
        return n + f(n/2)
    else:
        return f(n + 1)


for n in range(1, 100):
    print(n, f(n))

