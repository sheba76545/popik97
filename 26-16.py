file = open('26-16.txt')
k = int(file.readline().split()[0])
data = [tuple(map(int, line.split())) for line in file]
data.sort(key=(lambda x: x[0]), reverse=True)
data.sort(key=(lambda x: x[1] / x[0]))
print(sum(w for w, p in data[:k]))
print(max((t for t in data[:k]), key=lambda t: t[0]))


