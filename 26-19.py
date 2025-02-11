file = open('26-19.txt')
n = int(file.readline())
cenniki = sorted(int(line) for line in file)
cenniki_mini = [int(line) for line in cenniki if int(line) <= 210]
k = n - len(cenniki_mini)
cenniki_max = [int(line) for line in cenniki if int(line) > 210][k // 2:]
cenniki_sred = [int(line) for line in cenniki if int(line) > 210][:k // 2]
total = sum(cenniki_mini) + (sum(cenniki_sred) * 0.7) + sum(cenniki_max)
print(total)
print(max(cenniki_sred))