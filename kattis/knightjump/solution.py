def main():
    from heapq import heappush, heappop
    n = int(input())
    grid = [input() for _ in range(n)]

    q = []
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'K':
                heappush(q, (0, y, x))

    def maybe_add(steps, y, x):
        if y < 0 or x < 0 or y >= n or x >= n:
            return
        if grid[y][x] == '#':
            return
        heappush(q, (steps, y, x))

    been = set()
    while q:
        steps, y, x = heappop(q)
        if (y,x) in been:
            continue
        been.add((y,x))

        if x == 0 and y == 0:
            print(steps)
            return

        ns = steps+1
        maybe_add(ns, y-2, x-1)
        maybe_add(ns, y-2, x+1)
        maybe_add(ns, y+2, x-1)
        maybe_add(ns, y+2, x+1)
        maybe_add(ns, y-1, x-2)
        maybe_add(ns, y+1, x-2)
        maybe_add(ns, y-1, x+2)
        maybe_add(ns, y+1, x+2)

    print('-1')

main()
