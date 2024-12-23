f = open('24-9.txt')
s = []
text = f.readlines()
for i in text:
    if i.count('K') > i.count('U'):
        s.append(i)
print(s,len(s))
