def f(n):
    if n >= 2026:
        return n
    else:
        return 2 + n + f(n+2)


print(f(2021) - f(2022))
