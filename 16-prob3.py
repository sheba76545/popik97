import sys
sys.setrecursionlimit(2100)
def f(n):
    if n == 1:
        return 5
    else:
        return 2 * n + f(n-1)
print(f(2048) - f(1024))