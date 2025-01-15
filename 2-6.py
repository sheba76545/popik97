print('w x z y')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((x <= y) == (y <= (not w))) or ((not (z)) and w)) == False:
                    print(w, x, z, y)