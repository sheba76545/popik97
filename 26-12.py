file = open('26-12.txt')
lines = list(file)
max_weight = int(lines[0].split()[1])
gruz_priority = sorted((int(line) for line in lines[1:]
                        if (200 <= int(line) <= 220)),
                       reverse=True)
max_weight -= sum(gruz_priority)
default_gruz = sorted(int(i) for i in lines[1:] if
                      ((200 <= int(i) <= 220) == False))
total = 0
i = 0
while total <= max_weight:
    total += default_gruz[i]
    i += 1
i -= 1
print(i + len(gruz_priority))
total -= default_gruz[i] + default_gruz[i - 1]
maxi = [int(x) for x in lines[1:] if int(x) <= (max_weight - total)]
print(max(maxi))
