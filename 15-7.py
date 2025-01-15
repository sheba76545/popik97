def f(x, a):
    return ((x % 3 == 0) <= (x % 11 != 0)) or (x + a >= 80)


for a in range(1, 100):
    if all(f(x, a) for x in range(1, 200)):
        print(a)
        