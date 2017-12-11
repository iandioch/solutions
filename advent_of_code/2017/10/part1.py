lengths = list(map(int, input().split(',')))
nums = list(map(int, range(256)))

pos = 0
skip = 0

def flip(anums, start, length):
    new_nums = nums[:]
    for a in range(length):
        i = (start+a) % len(anums)
        j = (start + length - 1 - a) % len(anums)
        new_nums[j] = anums[i]
    return new_nums

for length in lengths:
    if length > len(nums):
        # 'Lengths larger than the size of the list are invalid.'
        print('Invalid', length, len(nums))
        continue
    start = pos
    new_nums = flip(nums, start, length)
    pos += length + skip
    pos %= len(nums)
    skip += 1
    nums = new_nums

print(nums[0] * nums[1])
