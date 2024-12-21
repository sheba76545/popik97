def K(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return K(a + 1, b) + K(a + 3, b)

answer = K(1, 9) * (K(9, 19) - K(9, 10)*K(10, 19))
print(answer)