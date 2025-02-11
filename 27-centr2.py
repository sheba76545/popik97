def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(cluster):
    xc, yc = None, None
    minr = 999
    for x1, y1 in cluster:
        r = sum(dist(x1, y1, x, y) for x, y in cluster)
        if r < minr:
            minr = r
            xc, yc = x1, y1
    return (xc, yc)


file = open('27-centr2.txt')
text = file.read().replace(',', '.')
lines = text.splitlines()
data = [list(map(float, line.split())) for line in lines]
cluster1 = [(x, y) for (x, y) in data if x > 1.5]
cluster2 = [(x, y) for (x, y) in data if x < 1.5]
x1, y1 = center(cluster1)
x2, y2 = center(cluster2)
print((x1 + x2) * 5_000, (y1 + y2) * 5_000)
