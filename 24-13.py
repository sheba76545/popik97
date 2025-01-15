f = open('24-13.txt')
text = f.read()
s = []
for i in range(len(text)-3):
    if (text[i] != text[i+1]) and (text[i+1] != text[i+2]) and (text[i+2] != text[i+3]) and (text[i] != text[i+2])\
    and (text[i] != text[i+3]) and (text[i+3] != text[i+1]):
        f = text[i] + text[i+1] + text[i+2] + text[i+3]
        s.append(f)
print(len(s))
