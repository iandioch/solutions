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

g = []

prefix = input().strip()
ans = 0
for i in range(128):
    s = '{}-{}'.format(prefix, i)
    k = knot(s)
    b = hex2bin(k)
    g.append(list(b))

num_iter = 0
while True:
    coord = None
    for y in range(0, 128):
        for x in range(0, 128):
            if g[y][x] == '1':
                coord = (y, x)
                break
        if coord is not None:
            break
    if coord is None:
        break
    num_iter += 1
    
    q = [coord]
    while len(q):
        y, x = q.pop()
        if g[y][x] != '1':
            continue
        g[y][x] = 'X'
        if y > 0:
            q.append((y-1, x))
        if x > 0:
            q.append((y, x-1))
        if y < 127:
            q.append((y+1, x))
        if x < 127:
            q.append((y, x+1))

print(num_iter)
