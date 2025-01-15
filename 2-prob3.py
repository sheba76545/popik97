print('y z x w ')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((x <= y) == (y <= w)) and (not(z <= x))) == True:
                    print(y,z, x, w)