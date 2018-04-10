from math import log, floor, pi

def stirling(n):
        return floor( ((n+0.5)*log(n) - n + 0.5*log(2*pi))/log(10) ) + 1

s = input().strip()
n = len(s)

if n == 1:
    if s == '1':
        print(1)
    elif s== '2':
        print(2)
    elif s=='6':
        print(3)
elif n == 3:
    if s == '120':
        print(5)
    elif s == '720':
        print(6)
else:
    for i in range(4, 1000000):
        if stirling(i) == n:
            print(i)
            break
