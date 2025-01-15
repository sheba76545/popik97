for x in '0123456789ABCDEFGH':
    a = int(f'''143{x}4''', 18) + int(f'''1{x}315''', 18)
    if a % 17 == 0:
        print(x, a / 17)
        
