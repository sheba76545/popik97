file = open('26-13.txt')
storage = int(file.readline().split()[0])
files = sorted(int(line) for line in file if
               int(line) % 2 == 0)
i = 0
total = 0
while total <= storage:
    total += files[i]
    i += 1
i -= 1
print(i)
total -= files[i] + files[i - 1]
maxi = [x for x in files if x <= (storage - total)]
print(max(maxi))
