def f(n):
    if n < 4:
        return n-1
    if (n >= 4) and (n % 3 != 0):
        return f(n-2) + f(n-3)
    else:
        return n + 2 * f(n-1)

print(f(25))

