f = open('24-2.txt')
text = f.read()
k = 1
max_k = 1
for i in range(1,len(text)):
    if text[i-1]==text[i]:
        k += 1
        max_k = max(k, max_k)
        f1 = text[i]
    else:
        k=1
print(text,max_k,f1)

