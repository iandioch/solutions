def main():
    l, n = map(int, input().split())
    ans = 1
    while True:
        k = l % n
        if k == 0:
            break
        n = n-k
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
