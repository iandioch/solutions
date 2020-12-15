def main():
    TARGET = 2020
    TARGET = 30000000
    last_occurance = [0]*TARGET

    curr = 1
    prev_num = None
    for num in map(int, input().split(',')):
        last_occurance[num] = curr
        prev_num = num
        curr += 1

    while curr <= TARGET:
        last = last_occurance[prev_num]
        if last == 0:
            num = 0
        else:
            num = curr - 1 - last

        last_occurance[prev_num] = curr - 1
        curr += 1
        prev_num = num

    print(prev_num)

main()
