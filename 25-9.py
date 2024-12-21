n = [] # Подходящие числа
for x in range(1500000, 3000000):
    ds = set() # Делители числа
    for d in range(1, round(x**0.5)+1):
     # Рассматриваем парные множители
        if x % d == 0:
            if d % 2 != 0:
                ds.add(d)
            if (x//d) % 2 != 0:
                ds.add(x//d)
        # Если делителей уже больше 3, то прекращаем работу цикла - такие числа нам не подходят
        if len(ds) > 7:
            break
    if len(ds) == 7:
        n.append(x)
print(len(n),
      n)

