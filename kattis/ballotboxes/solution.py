import math
from sys import stdin

def main():
    readline = stdin.readline
    ceil = math.ceil
    while True:
        ncities, nboxes = map(int, readline().split())
        if ncities < 0 and nboxes < 0:
            break
        pop = [float(readline()) for _ in range(ncities)]
        readline()

        lo = 1
        hi = max(pop)
        while hi - lo > 0.1:
            mid = lo + (hi - lo) / 2
            req = sum(ceil(p/mid) for p in pop)
            if req <= nboxes:
                hi = mid
            else:
                lo = mid
        print(ceil(lo))
                


if __name__ == '__main__':
    main()
