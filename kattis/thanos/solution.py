def main():
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        ans = 0
        while True:
            if a > c:
                print(ans)
                break
            a *= b
            ans += 1
            

if __name__ == '__main__':
    main()
