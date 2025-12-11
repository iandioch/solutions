import sys

memo = {}
def count_routes(routes, source, target):
    memok = (source, target)
    if memok in memo:
        return memo[memok]

    if source == target:
        return 1

    ans = 0
    for r in routes[source]:
        ans += count_routes(routes, r, target)
    memo[memok] = ans
    return ans


def main():
    routes = {}
    for line in sys.stdin.readlines():
        source, targets = line.split(':')
        routes[source] = []

        targets = targets[1:-1].split(' ')
        for t in targets:
            routes[source].append(t)

    print(count_routes(routes, source='you', target='out'))

main()
