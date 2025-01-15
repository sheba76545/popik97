for a in range(1, 200):
    k = 0
    for x in range(1, 101):
        if (x % a != 0) <= ((x % 16 == 0) <= (x % 24 != 0)):
            k += 1
    if k == 100:
        print(a)
        