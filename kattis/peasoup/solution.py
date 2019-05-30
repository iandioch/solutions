def main():
    n = int(input())
    found = False
    for _ in range(n):
        k = int(input())
        name = input()
        meals = set(input() for _ in range(k))
        if 'pea soup' in meals and 'pancakes' in meals:
            found = True
            print(name)
            break
    if not found:
        print('Anywhere is fine I guess')

main()
