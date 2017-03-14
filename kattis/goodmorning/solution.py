xpos = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 0,
    '5': 1,
    '6': 2,
    '7': 0,
    '8': 1,
    '9': 2,
    '0': 1
}

ypos = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 2,
    '8': 2,
    '9': 2,
    '0': 3
}
poss = set()
for i in range(1, 201):
    s = str(i)
    doable = True
    for j in range(1, len(s)): 
        if xpos[s[j]] < xpos[s[j-1]] or ypos[s[j]] < ypos[s[j-1]]:
            doable = False
    if doable:
        poss.add(i)

n = int(input())
for _ in range(n):
    m = int(input())
    if m in poss:
        print(m)
        continue
    i = 1
    while True:
        if m-i in poss:
            print(m-i)
            break
        if m+i in poss:
            print(m+i)
            break
        i += 1
