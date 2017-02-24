import sys
lines = sys.stdin.readlines()
i = 0

entered = {}

day = 1
while i < len(lines):
    i += 1
    owes = {}
    while lines[i] != 'CLOSE\n':
        parts = lines[i].split()
        if parts[0] == 'ENTER':
            entered[parts[1]] = int(parts[2])
        else:
            if parts[1] in owes:
                owes[parts[1]] += int(parts[2]) - entered[parts[1]]
            else:
                owes[parts[1]] = int(parts[2]) - entered[parts[1]]
            del entered[parts[1]]
        i += 1
    print("Day", day)
    for name in sorted(owes.keys()):
        print(name, "${:.2f}".format(owes[name]*0.1))
    print()
    day += 1
    i += 1
