from collections import deque
import sys

def main():
    PREAMBLE_SIZE = 25
    all_nums = []
    nums = deque([], PREAMBLE_SIZE)

    ans = None
    for line in sys.stdin.readlines():
        num = int(line)
        all_nums.append(num)

        if len(nums) < PREAMBLE_SIZE:
            nums.append(num)
            continue

        sumset = set()
        for n in nums:
            for m in nums:
                if n != m:
                    sumset.add(n+m)

        if num not in sumset:
            ans = num
            break
            
        nums.popleft()
        nums.append(num)


    print('ans:', ans)
    lo = 0
    hi = 1
    total = all_nums[0] + all_nums[1]
    while True:
        if total > ans:
            total -= all_nums[lo]
            lo += 1
        elif total < ans or lo == hi:
            hi += 1
            total += all_nums[hi]
        else:
            break

    domain = all_nums[lo:hi+1]
    print(domain)
    print(min(domain) + max(domain))

main()
