import sys
nums = list(sorted(int(s) for s in sys.stdin.readlines()))
start = 0
target = nums[-1] + 3
memo = [0]*(target+1)
memo[0] = 1
for n in nums:
    prefixes = 0
    for i in range(1, 4):
        if n - i >= 0:
            prefixes += memo[n-i]
    print('ways to get to {}: {}'.format(n, prefixes))
    memo[n] += prefixes
print(sum(memo[target-3:target+1]))
