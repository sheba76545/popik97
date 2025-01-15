for a in range(1, 50):
    k = 0
    for x in range(1, 201):
        for y in range(1, 201):
            if ((y + 2 * x) < a) or ((y + x) > 6) or ((y - x) < 4):
                k += 1
    if k == 200 ** 2:
        print(a)
        