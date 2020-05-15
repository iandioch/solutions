from collections import defaultdict

def main():
    with open('names.in', 'r') as f:
        names = [n.strip() for n in ''.join(f.readlines()).split(',')]
    with open('salaries.in', 'r') as f:
        salaries = [int(n.strip()) for n in ''.join(f.readlines()).split(',')]

    d = defaultdict(int)
    for i in range(len(names)):
        d[names[i]] += salaries[i]

    ranked = (sorted(d, key=lambda x: d[x], reverse=True))
    print(ranked[0])

main()
