def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x == 18:
        return 0
    else:
        return f(x+1, y) + f(x*2, y) + f(x*3, y)
print(f(1,12) * f(12,39))
