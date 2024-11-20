x=100*'9'
while '33333' in x or '999' in x:
    if '33333' in x:
        x=x.replace('33333','99',1)
    else:
        x=x.replace('999','3',1)
print(x)
