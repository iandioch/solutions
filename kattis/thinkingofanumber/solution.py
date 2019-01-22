from functools import reduce
import operator

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(max(a, b), min(a, b))

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        minn = None
        maxn = None
        divs = []
        for _ in range(n):
            a, b, c = input().split()
            c = int(c)
            if a == 'less':
                if maxn is None:
                    maxn = c
                else:
                    maxn = min(maxn, c)
            elif a == 'greater':
                if minn is None:
                    minn = c
                else:
                    minn = max(minn, c)
            elif a == 'divisible':
                divs.append(c)
        if maxn is None:
            print('infinite')
            continue
        tot = 0
        if minn is None:
            minn = 0
        minfact = 1
        lowest = 1
        if len(divs):
            lowest = reduce(lcm, divs)
        for i in range(lowest, maxn, lowest):
            if i <= minn:
                continue
            print(i, end=' ')
            tot += 1
        if tot == 0:
            print('none')
        else:
            print()

if __name__ == '__main__':
    main()
