import random
import heapq
from collections import deque

GATE_DISTS = []
TRANSFERS = []

def main():
    global TRANSFERS, GATE_DISTS

    n = int(input())
    GATE_DISTS = [list(map(int, input().split(','))) for _ in range(n)]
    TRANSFERS = [list(map(int, input().split(','))) for _ in range(n)]

    print('Gates & the number of free transfers from there:')
    for i in range(n):
        print(i, sum(1 for j in GATE_DISTS[i] if j==0))
    print('Flights, their size, and the largest transfer #s:')
    for i in range(n):
        print(i, 'transferring to', sum(1 for c in TRANSFERS[i] if c > 0), 'other flights, most popular:', sorted(map(lambda f: (f, TRANSFERS[i][f]), range(n)), key = lambda f: -f[1])[:5])

main()
