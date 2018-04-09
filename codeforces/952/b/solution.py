good = set(['great', 'great!', "don't think so", 'not bad', 'cool'])
grumpy = set(['are you serious', 'are you serious?', 'go die in a hole', 'worse', 'terrible', 'no way', "don't even"])

for i in range(10):
    print(i)
    ans = input().lower().strip()
    if ans in good:
        print('normal')
        break
    elif ans in grumpy:
        print('grumpy')
        break
