import sys

depths = list(map(int, sys.stdin.readlines()))
tot = sum(depths[:3])
ans = 0
for i in range(3, len(depths)):
    new_tot = tot - depths[i-3] + depths[i]
    if new_tot > tot:
        ans += 1
    tot = new_tot
print(ans)
