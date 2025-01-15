print('x w z y')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((not x) or (y) or (z)) and ((x) or (not z) or (not w))) == False:
                    print(x, w, z, y)
                    