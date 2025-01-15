print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((z == x) <= (w and z)) <= (((not y) and z) <= y)) == 0:
                    print(x, y, z, w)
