def main():
    from collections import defaultdict
    last_occurance = defaultdict(list)

    curr = 1
    prev_num = None
    for num in map(int, input().split(',')):
        last_occurance[num].append(curr)
        prev_num = num
        curr += 1
        pass

    while curr <= 2020:
        last = last_occurance[prev_num]
        if len(last) <= 1:
            # Last time was the first time.
            num = 0
        else:
            num = last[-1] - last[-2]
        print('{}: {} (prev = {})'.format(curr, num, prev_num))

        last_occurance[num].append(curr)
        curr += 1
        prev_num = num

main()
