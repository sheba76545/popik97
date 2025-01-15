from functools import cache
@cache
def f(n):
    s = 0
    s += (2*n + 1)
    if n > 1:
        s += (3*n - 8)
        s += f(n - 1)
        s += f(n - 4)
    return s
n = 0
while f(n) <= 5000000:
    n += 1
    print(n, f(n))
