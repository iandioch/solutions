import sys

def valid(s):
    t = s.strip().split()
    u = set(str(sorted(v)) for v in t)
    return len(u) == len(t)

ans = 0
for line in sys.stdin.readlines():
    if valid(line):
        ans += 1

print(ans)
