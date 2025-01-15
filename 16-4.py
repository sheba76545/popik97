from functools import cache
@cache
def f(n):
    if n == 1:
        return 1
    else:
       return f(n - 1) - (2 * g(n-1))
@cache
def g(n):
    if n == 1:
        return 1
    else:
        return f(n-1) + g(n-1) + n

print(g(36))