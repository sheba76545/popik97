print('z x y w ')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((x) and ((not (y)) and (z) and (not (w)) or (y) and (not (z)))) == True:
                    print(z, x, y, w)
