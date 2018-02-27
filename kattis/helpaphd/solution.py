n = int(input())
for _ in range(n):
    s = input()
    if s == 'P=NP':
        print('skipped')
    else:
        print(eval(s))
