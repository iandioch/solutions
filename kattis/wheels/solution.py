import fractions 
import math
from collections import deque

def main():
    gcd = fractions.gcd
    t = int(input())

    for _ in range(t):
        n = int(input())

        connected = [[] for _ in range(n)]
        pts = []
        for j in range(n):
            x, y, r = map(int, input().split())
            pts.append((x,y,r))
            for i in range(j):
                p, q, s = pts[i]
                if abs(math.sqrt((p-x)**2 + (q-y)**2) - (r+s)) < 0.0005:
                    connected[i].append(j)
                    connected[j].append(i)
        dist = [111111 for _ in range(n)]

        q = deque()
        q.append((0, 0))
        while len(q):
            curr, d = q.popleft()
            if d >= dist[curr]:
                continue
            dist[curr] = d
            d += 1
            for other in connected[curr]:
                if d < dist[other]:
                    q.append((other, d))

        for i in range(n):
            if dist[i] == 111111:
                print('not moving')
                continue
            clockwise = 'clockwise' if (dist[i] % 2 == 0) else 'counterclockwise'
            a, b = pts[0][-1], pts[i][-1]
            g = gcd(a,b)
            a, b = a//g, b//g
            if b == 1:
                print(a, clockwise)
            else:
                print('{}/{}'.format(a, b), clockwise)





main()
