n = int(input())
nums = list(map(int, (input() for _ in range(n))))

m = len(nums)
while True:
    found = True
    rems = set()
    for num in nums:
        rem = num % m
        if rem in rems:
            found = False
            break
        rems.add(rem)

    if found:
        print(m)
        break

    m += 1

