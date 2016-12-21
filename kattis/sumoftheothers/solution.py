import sys

for line in sys.stdin.readlines():
    nums = [int(x) for x in line.split()]
    tot = sum(nums)
    for n in nums:
        if n == tot - n:
            print (n)
            break
