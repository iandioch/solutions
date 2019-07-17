def main():
    h, w = map(int, input().split())
    xtot = 0
    n = 0
    lastline = ''
    for line in range(h):
        lastline = input().strip()
        for i, c in enumerate(lastline):
            if c != '.':
                xtot += i+0.5
                n += 1
    mid = xtot/n
    left, right = None, None
    for i, c in enumerate(lastline):
        if c != '.':
            right = i
            if left is None:
                left = i
    if mid < left:
        print('left')
    elif mid >= right+1:
        print('right')
    else:
        print('balanced')

main()

