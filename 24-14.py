f = open('24-14.txt')
text = f.read()
s = []
for i in range(len(text)-10):
    k = text[i]
    if text[i] <= text[i+1] <= text[i+2] <= text[i+3] <= text[i+4] <= text[i+5] <= text[i+6] <= text[i+7]:
        k += text[i+1] + text[i+2] + text[i+3] + text[i+4] + text[i+5] + text[i+6] + text[i+7]
        s.append(k)
    else:
        k = text[i]
print(s)

