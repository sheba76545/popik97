f=open('24-4.txt')
text=f.read()
a=text.split('S',)
a=str(a)
a1=a.split('T')
a1=str(a1)
a2=a1.split(',')
for h in a2:
    print(len(h))

