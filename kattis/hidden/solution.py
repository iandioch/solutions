seek, space = input().split()
ok = True
i = 0
j = 0
rest = set(seek[1:])
while j < len(space) and i < len(seek):
    if space[j] in rest and space[j] != seek[i]:
        ok = False
        break
    if space[j] == seek[i]:
        i += 1
        rest = set(seek[i+1:])
    j += 1

if i < len(seek):
    ok = False

if ok:
    print('PASS')
else:
    print('FAIL')
