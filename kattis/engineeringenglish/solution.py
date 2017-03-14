import sys

d = set()

for line in sys.stdin.readlines():
    s = []
    for word in line.split():
        if word.lower() in d:
            s.append('.')
        else:
            s.append(word)
        d.add(word.lower())
    print(' '.join(s))
