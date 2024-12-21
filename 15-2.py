def f(x,a):
    return (((not(x%a==0)) and (x%21==0)) <= (x%14==0))
for a in range(1,100):
    if all(f(x,a) for x in range(100)):
        print(a)