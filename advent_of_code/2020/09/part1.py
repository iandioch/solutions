from collections import deque
import sys

def main():
    PREAMBLE_SIZE = 25
    nums = deque([], PREAMBLE_SIZE)
    for line in sys.stdin.readlines():
        num = int(line)
        if len(nums) < PREAMBLE_SIZE:
            nums.append(num)
            continue

        sumset = set()
        for n in nums:
            for m in nums:
                if n != m:
                    sumset.add(n+m)

        if num not in sumset:
            print('ans:', num)
            break
            
        nums.popleft()
        nums.append(num)

main()
