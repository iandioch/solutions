import sys
from collections import deque

nums = [[int(x) for x in l.split(',')] for l in sys.stdin.readlines()]
mem = [[sys.maxint for x in xrange(len(nums[y]))] for y in xrange(len(nums))]

q = deque()
q.append((0,0,0))

ans = sys.maxint

while len(q)>0:
    x,y,c = q.popleft()
    #print x,y,c
    if c > mem[y][x] or c > ans:
        continue
    mem[y][x] = c
    c += nums[y][x]
    if x == len(nums[0])-1 and y == len(nums)-1:
        ans = min(ans, c)
        print c, ans
        continue
    if x < len(nums[0])-1 and c < mem[y][x+1]:
        q.append((x+1, y, c))
    if y > 0 and c < mem[y-1][x]:
        q.append((x, y-1, c))
    if y < len(nums)-1 and c < mem[y+1][x]:
        q.append((x, y+1, c))
    if x > 0 and c < mem[y][x-1]:
        q.append((x-1, y, c))

print ans
