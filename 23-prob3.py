def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif x == 22:
        return 0
    else:
        return f(x+1, y) + f(x*2, y)
print(f(1, 14) * f(14,54))
