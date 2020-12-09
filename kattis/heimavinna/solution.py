print(sum(1 if '-' not in s else (1 + int(s.split('-')[1]) - int(s.split('-')[0])) for s in input().split(';')))

