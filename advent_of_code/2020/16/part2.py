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

    tickets = []
    for line in sys.stdin.readlines():
        t = list(map(int, line.split(',')))
        tickets.append(t)

    valid = [all(any(c in rules[rule] for rule in rules) for c in t) for t in tickets]


    poss = {rule:set() for rule in rules}
    for rule in rules:
        for col in range(len(my_ticket)):
            # Check if col suits for rule
            rule_valid = True
            for i, ticket in enumerate(tickets):
                if not valid[i]:
                    continue
                if ticket[col] not in rules[rule]:
                    rule_valid = False
                    break
            if rule_valid:
                poss[rule].add(col)

    definite = {}
    while len(poss):
        for rule in poss:
            if len(poss[rule]) == 1:
                col = poss[rule].pop()
                definite[rule] = col
                del poss[rule]
                for other_rule in poss:
                    poss[other_rule].discard(col)
                break

    import functools
    import operator
    print(functools.reduce(operator.mul, (my_ticket[definite[rule]] for rule in rules if 'departure' in rule)))

main()
