def main():
    import heapq
    n = int(input())
    c = [int(input()) for _ in range(n)]
    q = []
    # (cost_so_far, curr_pos, size_of_last_jump)
    heapq.heappush(q, (c[1], 1, 1))

    visited = set()
    while len(q):
        cost, pos, jump = heapq.heappop(q)
        if (pos, jump) in visited:
            continue
        if pos == n-1:
            return cost
        visited.add((pos, jump))
        # try jump backwards
        backpos = pos-jump
        if backpos >= 0:
            heapq.heappush(q, (cost + c[backpos], backpos, jump))
        forwardpos = pos + jump + 1
        if forwardpos < n:
            heapq.heappush(q, (cost + c[forwardpos], forwardpos, jump + 1))
    return 0

if __name__ == '__main__':
    print(main())
