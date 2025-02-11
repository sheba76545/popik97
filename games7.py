import functools


@functools.cache
def game(x, y, level=0):
    if x + y >= 59:
        return 'go'
    if level > 10:
        return 'daun bozh'
    results = [game(x + 1, y, level + 1), game(x * 2, y, level + 1),
               game(x, y + 1, level + 1), game(x, y * 2, level + 1)]
    if any(r == "go" for r in results):
        return "W1"
    elif all(r == "W1" for r in results):
        return "L1"
    elif any(r == "L1" for r in results):
        return "W2"
    elif all(r == "W1" or r == "W2" for r in results):
        return "L2"



for i in range(1, 100):
    if game(5, i) == 'l1':
        print('19', i)
    if game(5, i) == 'w2':
        print('20', i)
    if game(5, i) == 'l2':
        print('21', i)
    print(i, game(5, i))



