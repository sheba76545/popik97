for i in range(700000,1000000000):
    M=[]
    for divs in range(2,i):
        if i%divs==0:
            M.append(divs)
            if sum(M)>1000000:
                print(i,sum(M))