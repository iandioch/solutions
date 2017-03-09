oh, ow, nh, nw = map(int, input().split())
for y in range(oh):
    s = input()
    for j in range(nh):
        print(''.join([c*nw for c in s]))
