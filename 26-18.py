file = open('26-18.txt')
babki = int(file.readline().split()[1])
cenniki = []
for line in file:
    cennik, letter = line.split()
    cenniki += [(int(cennik), letter)]
cenniki.sort()
k = 0
total = []
i = 0
while k != 95:
    if 'Z' in cenniki[i]:
        total.append(cenniki[i])
        k += 1
        i += 1
    else:
        i += 1
totaly = [(total[i])[0] for i in range(len(total))]
#print(sum(totaly) - 133 - 128 - 118 - 117 - 111 - 109 - 104 - 105 - 106 - 92 - 89 - 82 - 77 - 80, totaly, cenniki)
filtred_cenniki = sorted(num for num, letter in cenniki if letter == 'Q')
j = 0
while sum(totaly) >= 100000:
    max_index = totaly.index(max(totaly))
    totaly[max_index] = filtred_cenniki.pop(0)
    j += 1
print(100_000 - sum(totaly), 95 - j)