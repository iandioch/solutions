num_tests = int(input())
for _ in range(num_tests):
    num_prize, num_stickers = map(int, input().split())
    # tuple (sticker0, sticker4)->prize_value
    req = {}
    for _ in range(num_prize):
        n, *sticks, val = map(int, input().split())
        req[tuple(sticks)] = val
    q = {(i+1):v for i, v in enumerate(map(int, input().split()))}
    tot = 0
    for needed in req:
        a = min(q[i] for i in needed)
        tot += a*req[needed]
    print(tot)
