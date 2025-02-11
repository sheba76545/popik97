file = open('26-5.txt')
first_str = int(file.readline().split()[1])
prices = sorted((int(line) for line in file), reverse=True)[0:first_str]
print(prices[first_str - 1])
print(sum(prices) * 0.2)

