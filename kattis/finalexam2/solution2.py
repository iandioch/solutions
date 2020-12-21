def main():
    n = int(raw_input())
    ans = [raw_input() for _ in range(n)]
    print(sum(1 for i in xrange(n-1) if ans[i] == ans[i+1]))

main()
