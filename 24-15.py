file = open('24-15.txt')
text = file.readlines()
k = 0
for i in text:
    if i.count('K') > i.count('U'):
        k += 1
print(k)