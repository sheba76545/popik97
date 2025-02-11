import functools

@functools.cache
def game(x, y, level=0):
    if x + y >= 77: return "GO"
    if level > 4: return "Unknown"
    results = [game(x + 1, y, level+1), game(x * 2, y, level+1),
               game(x, y + 1, level+1), game(x, y * 2, level+1)]
    if any(r == "GO" for r in results):
        return "W1"
    elif all(r == "W1" for r in results):
        return "L1"
    elif any(r == "L1" for r in results):
        return "W2"
    elif all(r == "W1" or r == "W2" for r in results):
        return "L2"
    return "Unknown"


for i in range(1,100):
    print(i, game(7, i))