f=open('24-3.txt')
text=f.read()
k=0
maxi=1
for i in range(len(text)):
    if text[i]!='D':
        k+=1
        maxi=max(k,maxi)
    else:
        k=1



print(maxi-1,text)