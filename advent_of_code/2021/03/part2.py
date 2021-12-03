import sys

lines = [s.strip() for s in sys.stdin.readlines()]

def max_char_key(d):
    maxn = '1'
    if d['0'] > d['1']:
        maxn = '0'
    return maxn

def min_char_key(d):
    maxn = max_char_key(d)
    return '0' if maxn == '1' else '1'

def filter_nums(num_strs, i, char_key):
    if len(num_strs) == 1:
        return num_strs[0]
    d = {'0': 0, '1': 0}
    for s in num_strs:
        d[s[i]] += 1
    maxn = char_key(d)
    return filter_nums([s for s in num_strs if s[i] == maxn], i+1, char_key)

maxx = int(filter_nums(lines, 0, max_char_key), 2)
minx = int(filter_nums(lines, 0, min_char_key), 2)
print(maxx*minx)
