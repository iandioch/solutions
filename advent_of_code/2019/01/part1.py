import sys

ans = 0
for line in sys.stdin.readlines():
    ans += int(line)//3 - 2
print(ans)
