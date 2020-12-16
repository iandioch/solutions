import sys

def main():

    rules = {} # maps str name to set of valid ints
    line = input()
    while line != '':
        p = line.split(':')
        field = p[0]
        ranges = p[1].split(' or ')
        valid = set()
        for r in ranges:
            q = r.split('-')
            valid |= set(i for i in range(int(q[0]), int(q[1])+1))
        rules[field] = valid
        line = input().strip()

    _ = input() # "your ticket:"
    my_ticket = list(map(int, input().split(',')))
    _ = input() # empty line
    _ = input() # "nearby tickets:"

    print(rules)

    tickets = []
    for line in sys.stdin.readlines():
        t = list(map(int, line.split(',')))
        tickets.append(t)
        print(t)

    valid = [True for _ in range(len(tickets))]

    tot_bad_values = 0
    for i in range(len(tickets)):
        for col in tickets[i]:
            if all(col not in rules[r] for r in rules):
                valid[i] = False
                tot_bad_values += col
                break

    print(valid)
    print(tot_bad_values)

main()
