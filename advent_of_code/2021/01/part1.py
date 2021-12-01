import sys

ans = 0
prev = int(sys.stdin.readline())
for line in sys.stdin.readlines():
    curr = int(line)
    if curr > prev:
        ans += 1
    prev = curr
print(ans)
