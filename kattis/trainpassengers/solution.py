capacity, stations = map(int, input().split())

ok = True
curr = 0
for _ in range(stations):
    alight, board, left = map(int, input().split())
    if alight > curr:
        ok = False
        break
    curr -= alight
    curr += board
    if curr > capacity:
        ok = False
        break
    if left > 0 and (capacity - curr) > 0:
        ok = False
        break
if curr > 0:
    ok = False
if ok:
    print('possible')
else:
    print('impossible')
