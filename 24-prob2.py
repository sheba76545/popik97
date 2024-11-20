s = open('24-prob2.txt').readline().strip()
a = [-1,]

for i in range(len(s)-1):
    if s[i:i+2] == 'CD':
        a.append(i)

a.append(len(s)-1)

b = []

for x, y in zip(a, a[161:]):
    b.append(y-x)

print(max(b))