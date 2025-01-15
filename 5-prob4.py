for n in range(1,100):
    r = bin(n)[2:]
    if int(r) % 2 != 0 :
        r += '11'
    else :
        r += '00'
    r += str(r.count('1') % 2)
    print(n, int(r, 2))

