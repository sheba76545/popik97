
def f(x,y):
    if x<y:
        return f(x+1,y) + f(x+2,y) +f(x+3,y)
    if x==y:
        return 1
    if x>y:
       return 0

print(f(5,7)*f(7,11))