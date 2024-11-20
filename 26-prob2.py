f=[int(line) for line in open('26-prob2.txt')]
F=sorted(f)
s=[]
for x in range(100):
    for i in range(len(f)-1):
        while F[i]+5<=F[i+x]:
            s.append(F[i])




print(s)
