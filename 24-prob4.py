def find_longest_substring_with_three_F(file_name):
    # Чтение данных из файла
    with open(file_name, 'r') as file:
        text = file.read()

    max_len = 0  # Длина самой длинной подстроки с тремя буквами F
    count_F = 0  # Счётчик букв F в текущем окне
    start = 0  # Начало окна

    # Проходим по всему тексту
    for end in range(len(text)):
        if text[end] == 'F':
            count_F += 1

        # Когда в окне больше 3 букв F, сдвигаем начало
        while count_F > 3:
            if text[start] == 'F':
                count_F -= 1
            start += 1

        # Если в окне ровно 3 буквы F, проверяем длину подстроки
        if count_F == 3:
            max_len = max(max_len, end - start + 1)

    return max_len


# Пример использования
file_name = "24-prob4.txt"  # Имя файла, который нужно прочитать
result = find_longest_substring_with_three_F(file_name)
print(f"Длина самой длинной подстроки с тремя буквами F: {result}")
