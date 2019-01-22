def get_highest(goal, bids):
    best = None
    for bid in bids:
        if bid[0] > goal:
            return best
        best = bid
    return best

def main():
    n, goal = map(int, input().split())
    bids = []
    for _ in range(n):
        name, bid = input().split()
        bid = int(bid)
        bids.append((bid, name))
    bids.sort()
    g = goal
    ans = set()
    while g > 0:
        b = get_highest(g, bids)
        if b is None or b[1] in ans:
            print(0)
            return
        g -= b[0]
        ans.add(b[1])
    print(len(ans))
    print('\n'.join(ans))

    
if __name__ == '__main__':
    main()
