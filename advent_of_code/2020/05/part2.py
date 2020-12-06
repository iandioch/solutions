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
    return row * 8 + col, row, col

seat_ids = set()
d = {}
for line in sys.stdin.readlines():
    id_, row, col = get_id_for_seat(line.strip())
    seat_ids.add(id_)
    d[id_] = (row, col)

print(sorted(seat_ids))
print('\n'.join('{}: {}'.format(a, d[a]) for a in sorted(d)))

for i in range(min(seat_ids), max(seat_ids)):
    if (i not in seat_ids) and (i-1) in seat_ids and (i+1) in seat_ids:
        print(i)
        print(d[i-1])
        print(d[i+1])
