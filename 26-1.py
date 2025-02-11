def summ(number):
    summa = 0
    for i in str(number)[1:-1]:
        summa += int(i)
    return summa


k = 0
a = [i for i in range(100, 10000+1)]
a1 = [(summ(a[j]), a[j]) for j in range(len(a))]
a1.sort()
for k in range(1, len(a1)):
    print(k, a1[k])
