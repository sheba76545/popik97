from fnmatch import*
for i in range(0,10000000000,1983):
    if fnmatch(str(i),'1?3124*6'):
        print(i/1983)