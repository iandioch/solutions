import sys

def binsearch(lo, hi, pattern):
    # pattern is a list of booleans, where each is True if in the lower half
    # and False otherwise.
    for c in pattern:
        mid = lo + (hi - lo)//2
        if c:
            hi = mid
        else:
            lo = mid
    return lo

def get_id_for_seat(s):
    row_pattern = [c == 'F' for c in s[:7]]
    col_pattern = [c == 'L' for c in s[7:]]
    row = binsearch(0, 127, row_pattern) + 1
    col = binsearch(0, 7, col_pattern) + 1
    print(s, 'row:', row, 'col:', col)
    return row * 8 + col

max_id = 0
for line in sys.stdin.readlines():
    id_ = get_id_for_seat(line.strip())
    max_id = max(id_, max_id)

print(max_id)
