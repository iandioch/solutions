import sys

parent = {}
children = {}
weight = {}

def recursive_weight(p):
    ans = weight[p]
    for q in children[p]:
        ans += recursive_weight(q)
    return ans

def find_unbalanced(p):
    if len(children[p]) == 0:
        # leaf node
        return 0, [p]
    if len(children[p]) == 1:
        # must be the single child
        return find_unbalanced(children[p][0])
    if len(children[p]) == 2:
        ad, a = find_unbalanced(children[p][0])
        bd, b = find_unbalanced(children[p][1])
        if len(a) == 0:
            return bd, b
        return ad, a
    ws = {}
    for q in children[p]:
        w = recursive_weight(q)
        if w in ws:
            ws[w].append(q)
        else:
            ws[w] = [q]
    if len(ws) == 1:
        print(ws)
        return 0, [p]
    wrong = None
    good_val = None
    wrong_val = None
    for q in ws:
        if len(ws[q]) == 1:
            wrong = ws[q][0]
            wrong_val = q
        else:
            good_val = q
    diff, culprit = find_unbalanced(wrong)
    return good_val-wrong_val, culprit


for line in sys.stdin.readlines():
    parts = line.split()
    name = parts[0]
    if name not in parent:
        parent[name] = None
    children[name] = []
    weight_brackets = parts[1]
    weight_int = int(weight_brackets[1:-1])
    weight[name] = weight_int
    if '->' in line:
        a, b = line.split('->')
        dep = b.split(',')
        for d in dep:
            d = d.strip()
            parent[d] = name
            children[name].append(d)
            
for p in parent:
    if parent[p] is None:
        diff, culprit = find_unbalanced(p)
        print(weight[culprit[0]] + diff)


