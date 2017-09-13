d = {'duine eigin': -10}
while True:
    s = input()
    if s == '***':
        break
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

v = sorted(d, key=lambda x:d[x])
if d[v[-1]] == d[v[-2]]:
    print('Runoff!')
else:
    print(v[-1])
