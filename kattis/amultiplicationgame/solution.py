def winnable(n):
    stan = True
    p = 1
    while p < n:
        if stan:
            p *= 9
        else:
            p *= 2
        stan = not stan
    return not stan

def main():
    import sys
    for line in sys.stdin.readlines():
        n = int(line)
        if winnable(n):
            print('Stan wins.')
        else:
            print('Ollie wins.')
main()
