num_tests = int(input())
for _ in range(num_tests):
    days, months = map(int, input().split())
    num_so_far = 0
    ans = 0

    for m in map(int, input().split()):
        if m >= 13:
            if (num_so_far + 13) % 7 == 6:
                ans += 1
        num_so_far += m
    print(ans)
