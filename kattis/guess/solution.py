lo = 1
hi = 1001

while True:
    mid = (lo+hi)//2
    print(mid)
    s = input()
    if s == 'correct':
        break
    if s == 'lower':
        hi = mid
    elif s == 'higher':
        lo = mid
