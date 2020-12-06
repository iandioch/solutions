import sys

ans = 0
for line in sys.stdin.readlines():
    policy, pw = line.split(':')
    pos, letter = policy.split(' ')
    i, j= map(int, pos.split('-'))
    if (pw[i] == letter or pw[j] == letter) and pw[i] != pw[j]:
        ans += 1

print(ans)
