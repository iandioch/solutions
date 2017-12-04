import sys

def valid(s):
    t = s.strip().split()
    return len(set(t)) == len(t)

ans = 0
for line in sys.stdin.readlines():
    if valid(line):
        ans += 1

print(ans)
