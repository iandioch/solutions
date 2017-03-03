solved = {} # map question to time solved
tries_before_solving = {}
while True:
    p = input().split()
    if len(p) == 1:
        break
    time = int(p[0])
    q = p[1]
    if q in solved:
        continue
    if q in tries_before_solving:
        tries_before_solving[q] += 1
    else:
        tries_before_solving[q] = 1
    if p[2] == 'right':
        solved[q] = time

print(len(solved), end=' ')
print(sum([solved[x] + 20*(tries_before_solving[x]-1) for x in solved]))
