def search(x, y, lo, hi):
    if hi - lo < 10e-7:
        return lo
    p = lo + (hi-lo)/3
    a = p*(x-p*2)*(y-p*2)
    q = lo + (hi-lo)*2/3
    b = q*(x-q*2)*(y-q*2)
    if a > b:
        return search(x, y, lo, q)
    else:
        return search(x, y, p, hi)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    a = search(x, y, 0, min(x,y)/2)
    print(a*(x-2*a)*(y-2*a))
