import sys

digs = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

for line in sys.stdin.readlines():
    name = []
    tot = 0
    n = 0
    for word in line.split():
        if word[0] in digs:
            tot += float(word)
            n += 1
        else:
            name.append(word)
    print('{:.4f}'.format(tot/n), ' '.join(name))
