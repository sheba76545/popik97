print('z w y x')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((x<=(z==w)) or (not(y<=w))) == 0:
                    print(z,w,y,x)