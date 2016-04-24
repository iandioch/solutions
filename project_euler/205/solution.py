# count number of ways of getting each result for pete
fours = [1,2,3,4]

for i in xrange(8):
    n = []
    for f in fours:
        for j in xrange(1, 5):
            n.append(f+j)
    fours = n

f_counts = {}
for f in fours:
    if f in f_counts:
        f_counts[f] += 1
    else:
        f_counts[f] = 1

# count number of ways of getting each result for colin
sixes = [1,2,3,4,5,6]

for i in xrange(5):
    n = []
    for s in sixes:
        for j in xrange(1, 7):
            n.append(s+j)
    sixes = n

s_counts = {}
for s in sixes:
    if s in s_counts:
        s_counts[s] += 1
    else:
        s_counts[s] = 1

# count how many times pete wins
num_win = 0
total = 0
for i in f_counts:
    for j in s_counts:
        t = f_counts[i]*s_counts[j]
        total += t
        if j >= i:
            continue
        num_win += t

print '{:.7f}'.format((num_win+0.0)/total)
