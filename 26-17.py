file = open('26-17.txt')
k = int(file.readline().split()[1])
coords = [tuple(map(int, line.split())) for line in file]
coords.sort()
old_row = -1
k = 0
old_colon = 0
nlines = 0
for row, colon in coords:
    if row == old_row:
        if colon == old_colon + 1:
            k += 1
        else:
            if k > k:
                nlines += 1
        k = 0
    else:
        if nlines > max_nlines:
            max_nines
        k = 0

