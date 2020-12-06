def main():
    n = int(input())
    for _ in range(n):
        k, *o = map(int, input().split())
        ans = 1 - len(o) + sum(o)
        print(ans)

main()
