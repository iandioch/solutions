num_trans, num_pairs = map(int, input().split())
d = {}
for _ in range(num_trans):
    a, b = input().split()
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]

def reaches(start, end, seen):
    if start == end:
        return True
    if start not in d:
        return False
    seen.add(start)
    for v in d[start]:
        if v in seen:
            continue
        if reaches(v, end, seen):
            return True
    return False
    

for _ in range(num_pairs):
    a, b = input().split()
    if len(a) != len(b):
        print('no')
        continue
    ok = all(reaches(a[i], b[i], set()) for i in range(len(a)))
    if ok:
        print('yes')
    else:
        print('no')
