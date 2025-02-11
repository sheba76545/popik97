def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(cluster):
    xc, yc = None, None
    minr = float('+inf')
    for x1, y1 in cluster:
        r = sum(dist(x1, y1, x, y) for x, y in cluster)
        if r < minr:
            minr = r
            xc, yc = x1, y1
    return (xc, yc)

file = open('27-centr3.txt')
text = file.read().replace(',', '.')
lines = text.splitlines()
data = [list(map(float, line.split())) for line in lines]
cluster1 = [(x, y) for (x, y) in data if y < ((- 11/6) * x) + (8/3)]
cluster2 = [(x, y) for (x, y) in data if (y < 2) and (x > 1)]
cluster3 = [(x, y) for (x, y) in data if (y > ((- 11/6) * x) + (8/3)) and (y > 2)]
x1, y1 = center(cluster1)
x2, y2 = center(cluster2)
x3, y3 = center(cluster3)
print((x1 + x2 + x3) / 3 * 10000)
print((y1 + y2 + y3) / 3 * 10000)
