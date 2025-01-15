for A in range(1, 101):
    k = 0
    for x in range(1, 201):
        for y in range(1, 201):
            if (x > A) or (y > A) or ((2 * x + y) != 84):
                k += 1
    if k == 200 ** 2:
        print(A)

