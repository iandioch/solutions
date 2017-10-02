import sys

seen = set()
invalid = set()
blacklist = set()
proj = {'':set()}
curr = ''

for line in sys.stdin.readlines():
    line = line.strip()
    if line == '1':
        del proj['']
        for title in proj:
            proj[title] = proj[title] - blacklist
        titles = sorted(proj)
        titles = sorted(titles, key = lambda x: -len(proj[x]))
        for title in titles:
            print(title, len(proj[title]))
        seen = set()
        invalid = set()
        blacklist = set()
        proj = {'':set()}
        curr = '' 
        continue
    if line == '0':
        break
    if line[0].upper() == line[0]:
        invalid = invalid | proj[curr]
        proj[line] = set()
        curr = line
    else:
        if line in invalid:
            blacklist.add(line)
        proj[curr].add(line)
        seen.add(line)
