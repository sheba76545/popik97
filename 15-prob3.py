def f(x):
    return ((x % 7 == 0) <= (x % 6 != 0)) or (x + a >= 54)
for a in range(1,100):
    if all(f(x) == 1 for x in range(1,1000)):
        print(a)
        break