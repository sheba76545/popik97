f = open('24-11.txt')
text = f.read()
s = []
text = text.replace('DE', 'D E')
text = text.replace('BE', 'B E')
text = text.replace('CE', 'C E')
text = text.replace('AE', 'A E')
text = text.replace('EE', 'E E')
text = text.split()
for i in text:
    if 'EBCFEBCF' in i:
        s.append(i)
for w in s:
    print(len(w),w)