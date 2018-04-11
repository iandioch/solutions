def main():
    n = int(input())

    d = [int(x) for x in input().split()]

    left = [None] * n
    maxn = 0
    for i in range(n):
        if d[i] > maxn:
            maxn = d[i]
        left[i] = maxn

    ans = 0
    minn = maxn
    for i in range(n-1, -1, -1):
        if d[i] < minn:
            minn = d[i]
        if minn == left[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
