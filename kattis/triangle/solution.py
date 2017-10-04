# num triangles for each step in seq = 3^(n)
# perimeter of each triangle = 3/(2^(n-1))
# mult these = (3^(n+1))/(2^n)

import sys

curr = 1
for line in sys.stdin.readlines():
    n = int(line)
    val = (3**(n+1))//(2**n)
    ans = len(str(val))
    print('Case {}: {}'.format(curr, ans))
    curr += 1
