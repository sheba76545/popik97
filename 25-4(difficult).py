s=[]
k=0
for x in range(904528,997438):
    for d in range(1,997438**0,5):
        while k<5:
            if x%d==0:
                k+=1
                s.append(x,d)
print(s)
