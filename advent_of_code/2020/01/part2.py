import sys
nums = [int(n) for n in sys.stdin.readlines()]
numset = set(nums)

for i in range(len(nums)):
    a = nums[i]
    for j in range(i+1, len(nums)):
        b = nums[j]
        c = 2020 - a - b
        if c in numset:
            print(a*b*c)
