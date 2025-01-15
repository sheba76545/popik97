
from functools import lru_cache
def moves(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*3, b), (b*3, a)
@lru_cache(None)
def game(h):
    if sum(h) >= 103: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if any(game(m) == 'P1' for m in moves(h)): return 'V1'
for s in range(1, 97):
    if game((3, s)) == 'V1':
        print(s)
        break