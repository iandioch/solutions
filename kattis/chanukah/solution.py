def main():
    import sys
    read = sys.stdin.readline
    n = int(read())
    results = []
    for _ in range(n):
        id_, v = read().split()
        v = int(v)
        ans = v*(v+1)//2 + v
        results.append(f'{id_} {ans}')
    sys.stdout.write('\n'.join(results))

main()
