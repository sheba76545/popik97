for i in range(600, 141251):
    ds = set()  # Чётные делители
    for d in range(1, int(i ** 0.5) + 1):
        if i % d == 0:
            ds.add(d)
            ds.add(i // d)
            # Если кол-во превышает 4, то пропускаем
        if len(ds) > 5:
            break
    if len(ds) == 5:
        print(i,sorted(ds))