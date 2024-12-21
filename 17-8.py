a=[int(line) for line in open('17-8.txt')]
b=[a[i] + a[i+1] + a[i+2] + a[i+3] for i in range(len(a)-3) if (a[i] + a[i+1] + a[i+2] + a[i+3])==34847]

print(b)