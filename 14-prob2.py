
def sixth(a):
    k = 0
    while a>0:
        if a%6 == 0:
            k+=1
        a = a//6
    return k
for x in range(1,2031):
    a = 6**260+6**160+6**60-x
    if sixth(a) == 202:
        print(x,sixth(a))
