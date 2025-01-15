from sys import setrecursionlimit
setrecursionlimit(3000)


def f(n):
    if n == 1:
        return 2
    else:
        return 2 * n * f(n-1)


print(f(2020) / f(2017))
