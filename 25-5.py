k=0

for i in range(194567,194571):
    s = []
    for divs in range(1,199999,2):

        if i%divs==0:

            s.append(divs)
    print(s,i)
