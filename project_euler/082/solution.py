import sys

nums = [[int(x) for x in l.split(',')] for l in sys.stdin.readlines()]
mem = [[sys.maxint for x in xrange(len(nums[y]))] for y in xrange(len(nums))]

def minimal_route(start_x, start_y, curr):
    if curr >= mem[start_y][start_x]:
        return sys.maxint
    mem[start_y][start_x] = curr
    curr += nums[start_y][start_x]
    if start_x == len(nums)-1:
        return curr
    
    ans = sys.maxint
    if curr < mem[start_y][start_x+1]:
        ans = minimal_route(start_x+1, start_y, curr)
    if start_y > 0 and curr < mem[start_y-1][start_x]:
        ans = min(ans, minimal_route(start_x, start_y-1, curr))
    if start_y < len(nums)-1 and curr < mem[start_y+1][start_x]:
         ans = min(ans, minimal_route(start_x, start_y+1, curr))
    return ans

ans = sys.maxint
for i in xrange(len(nums)):
    ans = min(ans, minimal_route(0, i, 0))

print ans
    
