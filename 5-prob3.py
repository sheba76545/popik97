for n in range(100):
    r = bin(n)[2:]
    if n%2 == 0:
        r += '01'
    else:
        r += '10'
    r += str(r.count('1')%2)
    print(n,int(r, 2))
