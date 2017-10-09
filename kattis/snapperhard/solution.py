num_tests = int(input())
for test in range(1, num_tests+1):
    length, num = map(int, input().split())
    if num % (2 ** length) == (2 ** length)-1:
        print('Case #{}: ON'.format(test))
    else:
        print('Case #{}: OFF'.format(test))
