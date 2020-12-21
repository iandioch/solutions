def main():
    import sys
    n = int(sys.stdin.readline())
    ans = [sys.stdin.readline() for _ in range(n)]
    print(sum(1 for i in range(n-1) if ans[i] == ans[i+1]))

main()
