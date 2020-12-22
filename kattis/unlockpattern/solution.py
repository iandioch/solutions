def main():
    def dist(x1, y1, x2, y2):
        import math
        return math.sqrt((y2-y1)**2 + (x2-x1)**2)
    grid = [list(map(int, input().split())) for _ in range(3)]
    pos = {}
    for y in range(3):
        for x in range(3):
            pos[grid[y][x]] = (x, y)
    ans = 0
    for i in range(2, 10):
        ans += dist(*pos[i-1], *pos[i])
    print(ans)

main()
