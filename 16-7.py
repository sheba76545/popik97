import sys
sys.setrecursionlimit(3000)


def f(n):
    if n >= 2021:
        return n
    else:
        return n + f(n+1)


result = f(2017) - f(2019)
print(result)
