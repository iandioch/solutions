def main():
    n = int(input())
    d = {} # (name, val)
    for _ in range(n):
        name, val, bday = input().split()
        val = int(val)
        if bday not in d or d[bday][1] < val:
            d[bday] = (name, val)
    print(len(d))
    print('\n'.join(sorted(d[b][0] for b in d)))

main()
