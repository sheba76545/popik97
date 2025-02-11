file = open('26-14.txt')
n = int(file.readline())
files = sorted(map(int, file))[n // 10: - (n // 10)]
print(sum(files), max(files))
