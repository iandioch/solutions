import sys
m = list(map(int, sys.stdin))
f = 0
s = set()
ok = False
while not ok:
    for n in m:
        f += n
        if f in s:
            print(f)
            ok = True
            break
        s.add(f)
