reg_sizes = [2, 3, 5, 7, 11, 13, 17, 19, 5]
vals = [1, 2]
for size in reg_sizes[1:]:
    vals.append(vals[-1]*size)
max_val = 9699689
n = list(map(int, input().split())) + [0]
m = sum(n[i]*vals[i] for i in range(len(n)))
print(max_val - m)
