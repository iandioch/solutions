from collections import deque

def num(y, x, h, w, grid, visited):
    if visited[y][x]:
        return 0
    DIRS = ((0,1), (1,0), (0,-1), (-1, 0))
    valid = True
    ans = 1
    qu = deque()
    qu.append((y,x))
    visited[y][x] = True

    c = grid[y][x]
    while len(qu):
        j, i = qu.popleft()
        for d in DIRS:
            q = j + d[0]
            p = i + d[1]
            if q < 0 or p < 0 or q >= h or p >= w:
                continue
            if grid[q][p] < c:
                valid = False
            elif grid[q][p] == c and not visited[q][p]:
                qu.append((q,p))
                visited[q][p] = True
                ans += 1
    return ans if valid else 0

def main():
    w, h = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            ans += num(y, x, h, w, grid, visited)
    print(ans)

if __name__ == '__main__':
    main()
