def max_subarray(a):
    # kadane's algorithm
    max_ending_here = a[0]
    max_so_far = 0
    for x in a[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

n, p = map(int, input().split())
a = list(map(lambda x: int(x) - p, input().split()))
print(max_subarray(a))
