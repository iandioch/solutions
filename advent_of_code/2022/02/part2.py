import sys

def shapescore(c):
    d = {
            'A': 1,
            'B': 2,
            'C': 3,
            'X': 1,
            'Y': 2,
            'Z': 3,
    }
    return d[c]

def winningscore(i, j):
    if i == j:
        return 3
    if (i, j) in [(1, 2), (2, 3), (3, 1)]:
        return 6
    return 0

def getpair(i, des):
    #1 rock
    #2 paper
    #3 scissors
    if des == 'X': #lose
        d = {
            1: 3,
            2: 1,
            3: 2
        }
        return d[i]
    if des == 'Y': #draw
        return i
    d = {
        1: 2,
        2: 3,
        3: 1,
    }
    return d[i]

tot = 0
for line in sys.stdin.readlines():
    opponent, me = line.strip().split()
    i = shapescore(opponent)
    j = getpair(i, me)

    score = j + winningscore(i, j)
    tot += score
print(tot)

