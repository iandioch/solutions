def main():
    import sys
    n = int(input())
    ans = [1 for line in sys.stdin.readlines() if 'pink' in line.lower() or 'rose' in line.lower()]
    if len(ans) == 0:
        print('I must watch Star Wars with my daughter')
    else:
        print(len(ans))

main()
