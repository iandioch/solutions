import math

n, w, h = [int(q) for q in input().split()]
hyp = math.sqrt(w*w + h*h) + 0.01

for _ in range(n):
    if int(input()) < hyp:
        print('DA')
    else:
        print('NE')
