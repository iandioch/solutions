g = [list(map(int, input().split())) for _ in range(4)]

d = int(input())

if d == 0:
    # Left
    for j in range(4):
        fixed = set()
        changed = 1
        while changed > 0:
            changed = 0
            for i in range(1, 4):
                if g[j][i] == 0:
                    continue
                if g[j][i-1] == 0:
                    g[j][i-1] = g[j][i]
                    g[j][i] = 0
                    changed += 1
                    if i in fixed:
                        fixed.remove(i)
                        fixed.add(i-1)
                elif i not in fixed and (i-1) not in fixed and g[j][i-1] == g[j][i]:
                    g[j][i-1] *= 2
                    g[j][i] = 0
                    fixed.add(i-1)
                    changed += 1
elif d == 1:
    # Up
    for i in range(4):
        fixed = set()
        changed = 1
        while changed > 0:
            changed = 0
            for j in range(1, 4):
                if g[j][i] == 0:
                    continue
                if g[j-1][i] == 0:
                    g[j-1][i] = g[j][i]
                    g[j][i] = 0
                    changed += 1
                    if j in fixed:
                        fixed.remove(j)
                        fixed.add(j-1)
                elif j not in fixed and (j-1) not in fixed and g[j-1][i] == g[j][i]:
                    g[j-1][i] *= 2
                    g[j][i] = 0
                    fixed.add(j-1)
                    changed += 1
elif d == 2:
    # Right
    for j in range(4):
        fixed = set()
        changed = 1
        while changed > 0:
            changed = 0
            for i in range(2, -1, -1):
                if g[j][i] == 0:
                    continue
                if g[j][i+1] == 0:
                    g[j][i+1] = g[j][i]
                    g[j][i] = 0
                    changed += 1
                    if i in fixed:
                        fixed.remove(i)
                        fixed.add(i+1)
                elif i not in fixed and (i+1) not in fixed and g[j][i+1] == g[j][i]:
                    g[j][i+1] *= 2
                    g[j][i] = 0
                    fixed.add(i+1)
                    changed += 1
else:
    # Down
    for i in range(4):
        fixed = set()
        changed = 1
        while changed > 0:
            changed = 0
            for j in range(2, -1, -1):
                if g[j][i] == 0:
                    continue
                if g[j+1][i] == 0:
                    g[j+1][i] = g[j][i]
                    g[j][i] = 0
                    changed += 1
                    if j in fixed:
                        fixed.remove(j)
                        fixed.add(j+1)
                elif j not in fixed and (j+1) not in fixed and g[j+1][i] == g[j][i]:
                    g[j+1][i] *= 2
                    g[j][i] = 0
                    fixed.add(j+1)
                    changed += 1


for j in range(4):
    print(*g[j])
