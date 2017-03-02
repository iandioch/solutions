common = input()
n_groups = int(input())
groups = []
for group in range(n_groups):
    p = input().split()
    ok = False
    for w in p:
        if common[-len(w):] == w:
            ok = True
            break
    if ok:
        groups.append(p)

n_tests = int(input())
for test in range(n_tests):
    s = input()
    ok = False
    for g in groups:
        for w in g:
            if s[-len(w):] == w:
                ok = True
                break
        if ok:
            break
    if ok:
        print ('YES')
    else:
        print ('NO')
