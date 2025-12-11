import sys

memo = {}
def count_routes(routes, source, target, has_dac=False, has_fft=False):
    memok = (source, target, has_dac, has_fft)
    if memok in memo:
        return memo[memok]

    if source == target:
        if has_dac and has_fft:
            return 1
        return 0
    elif source == 'dac':
        has_dac = True
    elif source == 'fft':
        has_fft = True

    ans = 0
    for r in routes[source]:
        ans += count_routes(routes, r, target, has_dac, has_fft)
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

    print(count_routes(routes, source='svr', target='out'))

main()
