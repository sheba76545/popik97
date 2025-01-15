from fnmatch import *
for x in range(0, 10 ** 10, 1983):
    if fnmatch(str(x), '1?3124*6'):
        print(x, x / 1983)