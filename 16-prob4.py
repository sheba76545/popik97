from sys import setrecursionlimit
setrecursionlimit(3000)


def f(n):
    if n < 2:
        return 1
    if (n > 1) and (n % 2 == 0):
        return 2 * n * f(n-1)
    else:
        return f(n-1) - 1


print(f(2903) // f(2900))
