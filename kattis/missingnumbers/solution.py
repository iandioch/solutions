n = int(input())
nums = set([int(input()) for _ in range(n)])
maxn = max(nums)
if maxn == len(nums):
    print('good job')
else:
    for i in range(1, maxn):
        if i not in nums:
            print(i)
