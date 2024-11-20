for r in range(63):
    n=bin(r)[2:]
    f=n.count('1')
    f=n+str(int(f)%2)
    f = f+'0'
    print(r,int(f,2))
