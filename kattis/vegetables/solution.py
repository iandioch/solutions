import heapq
from math import ceil

def main():
    ratio, n = input().split()
    ratio = float(ratio)
    n = int(n)
    w = map(int, input().split())

    # -piece weight, veg weight, num cuts
    q = []
    for v in w:
        heapq.heappush(q, (-v, v, 0))

    ncuts = 0

    v, t, c = heapq.heappop(q)
    while (heapq.nlargest(1, q)[0][0]/v) < ratio + 0.0001:
        ncuts += 1
        c += 1
        v, t, c = heapq.heappushpop(q, (-(t/(c+1)), t, c))
    print(ncuts)

main()
