def step_cost(d):
    # Sum of d entries of linearly increasing arithmetic series from 1 to d
    return d*(1+d)//2

def calc_cost(nums, d):
    return sum(step_cost(abs(n-d)) for n in nums)

def main():
    nums = list(map(int, input().split(',')))
    lo = min(nums)
    hi = max(nums)

    print(min(calc_cost(nums, d) for d in range(lo, hi+1)))

main()
