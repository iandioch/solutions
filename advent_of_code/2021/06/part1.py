def main():
    PRINT = False

    nums = list(map(int, input().split(',')))

    num_days = 80
    for d in range(num_days):
        curr_len = len(nums)
        for i in range(curr_len):
            if nums[i] == 0:
                nums[i] = 7
                nums.append(8)
            nums[i] -= 1

        if PRINT:
            print(f'After {d+1} days: {",".join(map(str, nums))}')

    print(len(nums))

main()

