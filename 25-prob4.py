from fnmatch import fnmatch
for x in range(0, 10 ** 10, 2023):
    if fnmatch(str(x), '1?5719*6'):
        print(x, x / 2023)
