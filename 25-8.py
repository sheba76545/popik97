def is_prime(number): # функция для проверки простоты числа
    if number == 1: return False
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            return False
    return True


def divs(x): # функция, которая возвращает список делителей числа
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
ans = []
for x in range(318216,369453):
    d = [i for i in divs(x) if is_prime(i)] # список, в котором хранятся только простые делители числа
    if len(d) == 3:
        if d[0] % 10 == d[1] % 10 == d[2]%10 and d[0]*d[1]*d[2] == x: # если все простые делители оканчиваются на одну цифру и их произведение равно числу
            ans += [x]
print(len(ans),min(ans))