import sys
import heapq

def shortest_path(grid, start, target):
    q = []
    heapq.heappush(q, (-grid[start[1]][start[0]], start))
    memo = {}
    while len(q):
        risk, pos = heapq.heappop(q)
        x, y = pos
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            continue

        risk += grid[y][x]
        if pos in memo:
            if memo[pos] <= risk:
                continue
        memo[pos] = risk
        heapq.heappush(q, (risk, (x+1, y)))
        heapq.heappush(q, (risk, (x-1, y)))
        heapq.heappush(q, (risk, (x, y+1)))
        heapq.heappush(q, (risk, (x, y-1)))
    return memo[target]


def main():
    grid = []
    for line in sys.stdin.readlines():
        grid.append(list(map(int, line.strip())))

    print(shortest_path(grid, (0, 0), (len(grid[0])-1, len(grid)-1)))

main()
