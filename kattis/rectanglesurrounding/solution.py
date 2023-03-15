import sys

def main():
    lines = [s.strip() for s in sys.stdin.readlines()]
    p = 0
    while True:
        n = int(lines[p])
        if n == 0:
            break
        p += 1

        grid = [[False for _ in range(501)] for _ in range(501)]

        tot = 0
        for _ in range(n):
            s = list(map(int, lines[p].split()))
            ll, ur = (s[0], s[1]), (s[2], s[3])
            for x in range(ll[0], ur[0]):
                for y in range(ll[1], ur[1]):
                    grid[x][y] = True
            p += 1
        tot = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    tot += 1
        print(tot)
        if p >= len(lines)-1:
            break

main()
