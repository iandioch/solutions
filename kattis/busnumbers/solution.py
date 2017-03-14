n = int(input())
m = sorted(map(int, input().split()))
m.append(1239871263)

prev = m[0]
length = 1

ans = []
i = 1
while i < len(m):
    curr = m[i]
    if curr == prev+1:
        length += 1
    else:
        if length >= 3:
            ans.append('{}-{}'.format(m[i-length], m[i-1]))
        elif length == 2:
            ans.append(m[i-2])
            ans.append(m[i-1])
        else:
            ans.append(m[i-1])
        length = 1
    prev = curr
    i += 1

print(' '.join([str(i) for i in ans]))
