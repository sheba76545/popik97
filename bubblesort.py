k = 0
array = [4, 3, 2, 1]
n = len(array)
for i in range(n):
    for j in range(n - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            k += 1
print(array, k)