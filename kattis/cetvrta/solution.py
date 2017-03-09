xs = set()
ys = set()
for i in range(3):
    p = [int(n) for n in input().split()]
    if p[0] in xs:
        xs.remove(p[0])
    else:
        xs.add(p[0])
    if p[1] in ys:
        ys.remove(p[1])
    else:
        ys.add(p[1])

print(xs.pop(), ys.pop())
