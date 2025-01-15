a = 124 * '2' + 19 * '1'
while ('222' in a) or ('111' in a):
    if '222' in a:
        a = a.replace('222', '1', 1)
    if '111' in a:
        a = a.replace('111', '2', 1)
print(a)


