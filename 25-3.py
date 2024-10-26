from fnmatch import*
for x in range(0,10**8,33):
    if fnmatch(str(x),'13*02?87'):
        print(x,x//33)