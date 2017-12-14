from functools import reduce

def knot(s):
    lengths = list(map(ord, s.strip())) + [17, 31, 73, 47, 23]
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

    for _ in range(64):
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

    sparse_hash = nums
    dense_hash = []
    for i in range(16):
        n = reduce(lambda a, b: a^b, sparse_hash[i*16:(i+1)*16])
        dense_hash.append(n)
    return (''.join([format(i, '02x') for i in dense_hash]))

def hex2bin(h):
    return bin(int(h, 16))[2:].zfill(128)


prefix = input().strip()
ans = 0
for i in range(128):
    s = '{}-{}'.format(prefix, i)
    k = knot(s)
    b = hex2bin(k)
    for e in b:
        if e == '1':
            ans += 1

print(ans)
