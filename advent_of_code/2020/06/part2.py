import sys

def count_qs(group):
    qs = set(group[0])
    for line in group[1:]:
        qs = qs & set(line)
    return len(qs)


ans = 0
group = []
for line in sys.stdin.readlines():
    line = line.strip()

    if len(line) == 0:
        ans += count_qs(group)
        group = []
    else:
        group.append(line)

ans += count_qs(group)
print(ans)
