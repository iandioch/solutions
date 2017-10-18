MAX = 25

# correct number of smalls
def h(n):
    ans = 0
    side = 1
    while side*3 <= n:
        # find out how many hexes of side length `side` will fit in the triangle
        for y in range(side+1, n+2-side):
            m = (y - 2*side)
            if m < 0:
                continue
            # a hex of side T has T rotations that are possible too.
            ans += m*(side)
        side += 1
    return ans

ans = 0
for i in range(3, 12346):
    ans += h(i)
print(ans)
