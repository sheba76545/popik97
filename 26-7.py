file = open("kurs-26-4.txt")
N = int(file.readline())
data = sorted(map(int, file))
mean = sum(data) / N
median = data[N // 2]
A = [x for x in data if mean <= x <= median]
print(len(A))
