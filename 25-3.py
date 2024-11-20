def f(n):
    s = 0
    for i in range(1,3):
        s = s + n % 10
        n = n // 10
    return(s)
print(f(2018))