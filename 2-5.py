print('x z y w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((x and z) or ((not w or x) == (not z or y))) == False:
                    print(x, z, y, w)
