f = open('24-1.txt')
text=f.read()
m=0
text=text.replace('SR','S R')
text=text.replace('RS','R S')
text=text.replace('TS','T S')
text=text.replace('ST','S T')
words=text.split()
if 'S' in words:
    m=max(len(w) for w in words)
print(m,"S"*220)

