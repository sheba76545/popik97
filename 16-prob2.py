import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n<2:
        return 1
    elif ((n>1) and (n%2==0)):
        return 2*n*F(n-1)
    elif ((n>1) and (n%2==1)):
        return F(n-1)-1
print(F(2903)//F(2900))