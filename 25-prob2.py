from fnmatch import *
for x in range(0,10000000000,2023):
    if fnmatch(str(x),'1?5719*6'):
        print(x,x//2023)