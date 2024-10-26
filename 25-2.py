from fnmatch import*
for x in range(0,10**9,27):
    if fnmatch(str(x),'1234?67?8'):
        print(x,x//27)