for x in '0123456789abcdef':
    if (int(f'153{x}4', 16) + int(f'1{x}325', 16)) % 15 == 0:
        print(x, (int(f'153{x}4', 16) + int(f'1{x}325', 16)) / 15)
