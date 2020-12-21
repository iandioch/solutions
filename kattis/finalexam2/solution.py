def main():
    n = int(input())
    ans = [input() for _ in range(n)]
    print(sum(1 for i in range(n-1) if ans[i] == ans[i+1]))

main()
