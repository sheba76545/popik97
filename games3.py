# 1 куча #
def moves(p):
    return [p + 1, p * 2]


gp = range(1, 149)
go = range(149, 1000)
w1 = [p for p in gp if any(gamepoints in go for gamepoints in moves(p))]
l1 = [p for p in gp if all(gamepoints in w1 for gamepoints in moves(p))]
w2 = [p for p in gp if any(gamepoints in l1 for gamepoints in moves(p))]
l2 = [p for p in gp if p not in l1
     and all(gamepoints in w1 or gamepoints in w2 for gamepoints in moves(p))]
print(*l1)
print(*w2)
print(*l2)