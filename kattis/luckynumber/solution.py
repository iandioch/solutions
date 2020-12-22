def main():
    n = int(input())

    nums = [i for i in range(1, 10)]
    for i in range(2, n+1):
        newnums = []
        for num in nums:
            for j in range(10):
                newnum = (num*10)+j
                if newnum % i == 0:
                    newnums.append(newnum)
        nums = newnums
    print(len(nums))

main()
