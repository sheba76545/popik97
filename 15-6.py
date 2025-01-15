for a in range(1, 100):
    k = 0
    for x in range(1, 101):
        if ((x % 3 == 0) <= (x % 9 != 0)) or (x + a >= 108):
            k += 1
    if k == 100:
        print(a)
