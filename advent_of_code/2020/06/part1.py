import sys

def count_qs(group):
    qs = set()
    for line in group:
        qs.update(line)
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
