import sys
d = [('A',), ('A#', 'Bb'), ('B',), ('C',), ('C#', 'Db'), ('D',), ('D#', 'Eb'), ('E',), ('F',), ('F#', 'Gb'), ('G',), ('G#', 'Ab')]

casenum = 1
for line in sys.stdin.readlines():
    p = line.split()
    found = []
    for t in d:
        if p[0] in t:
            alt = [u for u in t if u != p[0]]
    if len(alt) == 0:
        print('Case {}: UNIQUE'.format(casenum))
    else:
        print('Case {}: {} {}'.format(casenum, alt[0], p[1]))
    casenum += 1
