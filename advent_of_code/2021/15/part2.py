import sys
import heapq

def shortest_path(grid, start, target):
    q = []
    heapq.heappush(q, (-grid[start[1]][start[0]], start))
    memo = {}

    num_repeats = 5

    base_width = len(grid[0])
    base_height = len(grid)
    width = base_width*num_repeats
    height = base_height*num_repeats

    def get_risk(x, y):
        base = grid[y%base_height][x%base_width]
        add = x//base_width + y//base_height
        risk = base+add - 1
        return risk%9 +  1

    while len(q):
        risk, pos = heapq.heappop(q)
        x, y = pos
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        risk += get_risk(x, y)
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

    print(shortest_path(grid, (0, 0), (5*len(grid[0])-1, 5*len(grid)-1)))

main()
