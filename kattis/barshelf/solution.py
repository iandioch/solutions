def main():
    import sys
    read = sys.stdin.readline
    n = int(read())

    ans = 0

    nums = list(map(int, read().split()))

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] >= 2*nums[j] and nums[j] >= 2*nums[k]:
                    ans += 1

    print(ans)

main()
