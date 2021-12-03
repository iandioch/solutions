from collections import defaultdict

def main():
    a, b, c, d = map(int, input().split())

    lhs = defaultdict(list)
    rhs = defaultdict(list)

    lhs[a+b].append('+')
    lhs[a*b].append('*')
    lhs[a-b].append('-')
    if b != 0:
        lhs[a//b].append('/')
    rhs[c+d].append('+')
    rhs[c*d].append('*')
    rhs[c-d].append('-')
    if d != 0:
        rhs[c//d].append('/')


    ans = []
    for p in lhs:
        for q in rhs:
            if p == q:
                for i in lhs[p]:
                    for j in rhs[q]:
                        ans.append((i, j))

    if not len(ans):
        print('problems ahead')
        return

    for ops in sorted(ans):
        print(a, ops[0], b, '=', c, ops[1], d)

main()
