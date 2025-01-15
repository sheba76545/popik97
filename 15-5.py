for A in range(1, 11):
    k = 0
    for x in range(1, 201):
        for y in range(1, 201):
            if ((6 * y - 2 * x) > A) or ((x + 4 * y) < 80) or ((2 * y - 3 * x) < -72):
                k += 1
    if k == 200 ** 2:
        print(A)

