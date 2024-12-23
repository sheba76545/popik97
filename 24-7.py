f = open('24-7.txt')
s = []
e = []
text = f.read()
text = text.replace('RS', 'R S')
text = text.replace('SR', 'S R')
text = text.replace('RT', 'R T')
text = text.replace('TR', 'T R')
text = text.split()
for i in range(len(text)):
    if 'R' in text[i]:
        s.append(text[i])
for w in s:
    e.append(w)
print(max(e))
