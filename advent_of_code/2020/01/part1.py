import sys
nums = [int(n) for n in sys.stdin.readlines()]
numset = set(nums)
for n in nums:
    if 2020-n in numset:
        print(n * (2020-n))
