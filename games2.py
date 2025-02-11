# 1 куча #
def moves(p):
    return [p+1, p*2]


GP = range(1, 29)
GO = range(29, 28*2 + 1)
W1 = [p for p in GP if any(ep in GO for ep in moves(p))]
L1 = [p for p in GP if all(ep in W1 for ep in moves(p))]
W2 = [p for p in GP if any(ep in L1 for ep in moves(p))]
L2 = [p for p in GP if p not in L1
        and all(ep in W1 or ep in W2 for ep in moves(p))]
print(L1)
print(W2)
print(L2)
