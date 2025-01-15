from sys import setrecursionlimit
setrecursionlimit(2600)


def f(n):
    if n < 3:
        return 1
    if (n >= 3) and (n % 2) == 0:
        return 2 * n + f(n - 2)
    else:
        return f(n-1) - 2


print(f(2554) - f(2544))

