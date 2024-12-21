# рассчет значений до n-нного числа Фиббоначи
n = int(input())
k = [0, 1] + [None] * (n - 1)
for i in range(2, n+1):
    k[i] = k[i-1] + k[i-2]
print(k)
