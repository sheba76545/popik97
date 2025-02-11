def T(p):
    x, y = p
    return [(x + 1, y), (x*2, y), (x, y + 1), (x, y*2)]


GO = {(x, y) for x in range(1, 63 * 2) for y in range(63 - x, 63 * 2)}
G = {(x, y) for x in range(1, 63) for y in range(63 - x)}
W1 = {p for p in G if any(ep in GO for ep in T(p))}
L1 = {p for p in G if all(ep in W1 for ep in T(p))}
W2 = {p for p in G if any(ep in L1 for ep in T(p))}
L2 = {p for p in G-L1 if all(ep in W1 | W2 for ep in T(p))}
print([s for s in range(63) if (7, s) in W2])
print([s for s in range(63) if (7, s) in L2])
