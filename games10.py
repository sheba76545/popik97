def game(x, y, lvl=0):
    if x + y >= 38:
        return 'go'
    if lvl > 5:
        return('dauuuuuun')
    results = [game(x + 2, y, lvl + 1), game(x + y, y, lvl + 1),
               game(x, y + 2, lvl + 1), game(x, y + x, lvl + 1)]
    if any(r == "go" for r in results):
        return "w1"
    elif all(r == "w1" for r in results):
        return "l1"
    elif any(r == "l1" for r in results):
        return "w2"
    elif all(r == "w1" or r == "w2" for r in results):
        return "l2"


for i in range(1, 20):
    if game(8, i) == 'l1':
        print('19', i)
    if game(8, i) == 'w2':
        print('20', i)
    if game(8, i) == 'l2':
        print('21', i)
        
