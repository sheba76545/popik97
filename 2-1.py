print('z y x w ')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((not(x)) and (not(y))) or (y == z) or (not(w))) == False:
                    print(z,y,x,w)