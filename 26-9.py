file = open('26-9.txt')
mesto = int(file.readline().split()[0])
files = sorted(int(line) for line in file)
i = 0
total = 0
while total <= mesto:
    total += files[i]
    i += 1
i -= 1
print(i)
total -= files[i] + files[i - 1]
m = [x for x in files if x <= (mesto - total)]
print(max(m))
