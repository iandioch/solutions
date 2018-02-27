s = input().split()
v = set()
ok = True
for w in s:
    if w in v:
        ok = False
        break
    v.add(w)
if ok:
    print('yes')
else:
    print('no')
