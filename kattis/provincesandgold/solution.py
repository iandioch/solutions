victory = [('Province', 8, 6), ('Duchy', 5, 3), ('Estate', 2, 1)]
treasure = [('Gold', 6, 3), ('Silver', 3, 2), ('Copper', 0, 1)]

a, b, c = map(int, input().split())
tot = a*3 + b*2 + c

vic = None
for v in victory:
    if tot >= v[1]:
        vic = v[0]
        break

tre = None
for t in treasure:
    if tot >= t[1]:
        tre = t[0]
        break

if vic is not None:
    print('{} or {}'.format(vic, tre))
else:
    print(tre)
