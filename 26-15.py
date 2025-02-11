file = open('26-15.txt')
k = int(file.readline().split()[1])
scores = sorted((map(int, file)), reverse=True)
otlichnichki = scores[:k]
horoshenkie = scores[k:(2 * k)]
print(sum(horoshenkie) // k)
print(sum(otlichnichki) // k)