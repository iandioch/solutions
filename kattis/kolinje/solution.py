def solve(prev_a, prev_b, curr_a, curr_b):
    # prev_a + prev_b*X >= curr_a + curr_b*X
    # X*(prev_b - curr_b) >= curr_a - prev_a
    if (prev_b - curr_b) == 0:
        if curr_a > prev_a:
            return False, None, None
        else:
            return True, None, None # curr_a >= prev_a
    elif (prev_b - curr_b) > 0:
        lower_x = (curr_a - prev_a) / (prev_b - curr_b)
        return True, lower_x, None
    else:
        upper_x = (curr_a - prev_a) / (prev_b - curr_b)
        return True, None, upper_x


n = int(input())

a = [0 for _ in range(n)]
b = [0 for _ in range(n)]

for i in range(n):
    a[i], b[i] = map(int, input().split())

ok = True
lowers, uppers = [], []
for i in range(1, n):
    valid, lower, upper = solve(a[i-1], b[i-1], a[i], b[i])
    if not valid:
        ok = False
        break
    if lower is not None:
        lowers.append(lower)
    if upper is not None:
        uppers.append(upper)

lower = max(lowers)
upper = min(uppers)
if not ok:
    print(-1)
elif lower <= upper:
    print(sum(b)*lower)
else:
    print(-1)
