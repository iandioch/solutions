import sys
nums = [0] + list(sorted(int(s) for s in sys.stdin.readlines()))
diffbucket = [-100, 0, 0, 0]
for i in range(1, len(nums)):
    diffbucket[nums[i] - nums[i-1]] += 1
diffbucket[3] += 1
print(diffbucket[1]*diffbucket[3])
