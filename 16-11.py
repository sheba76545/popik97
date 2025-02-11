def f(n):
    if n == 0:
        return 1
    if (n > 0) and (n % 3 == 0):
        return (n / 3) + f(n / 3)
    else:
        return (n % 3) + f(n - 1)


for n in range(10000):
    if f(n) == 2017:
        print(n, f(n))
