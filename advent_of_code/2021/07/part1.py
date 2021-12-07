def calc_cost(nums, d):
    return sum(abs(n-d) for n in nums)

def main():
    nums = list(map(int, input().split(',')))
    lo = min(nums)
    hi = max(nums)

    print(min(calc_cost(nums, d) for d in range(lo, hi+1)))

main()
