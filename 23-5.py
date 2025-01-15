def f(x,y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x == 24:
        return 0
    else:
        return f(x+1, y) + f(x * 2, y) + f(x ** 2, y)
print(f(2, 16) * f(16, 38))