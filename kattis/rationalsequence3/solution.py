from math import log

p2 = [(2**i)-1 for i in range(33)]

def get_at(n):
    if n == 1:
        return 1, 1
    for highest_pow2 in range(len(p2)):
        if p2[highest_pow2] >= n:
            break
    p = p2[highest_pow2-1] # number in previous row
    m = n - p - 1 # number to this element's left
    parent_id = p2[highest_pow2-2] + 1 + m//2
    parent = get_at(parent_id)
    if m % 2 == 0:
        return parent[0], parent[0]+parent[1]
    return parent[0] + parent[1], parent[1]

tests = int(input())
for test in range(1, tests+1):
    _, n = map(int, input().split())
    a, b = get_at(n)
    print('{} {}/{}'.format(test, a, b))
