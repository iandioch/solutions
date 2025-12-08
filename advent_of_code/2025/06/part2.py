import sys

def product(nums):
    ans = nums[0]
    for n in range(1, len(nums)):
        ans *= nums[n]
    return ans

def main():
    inp = []
    for line in sys.stdin.readlines():
        p = line.strip('\n')
        inp.append(p)

    ans = 0
    n = 0
    while n < len(inp[0]):
        op = inp[-1][n]
        print(n, op)
        row_w = 1
        while True:
            if n + row_w == len(inp[0]):
                row_w += 1
                break
            elif inp[-1][n + row_w] != ' ':
                break
            row_w += 1

        nums = []
        for i in range(n, n+row_w-1):
            num = ''
            for j in range(0, len(inp)-1):
                print(i, j, inp[j][i])
                if inp[j][i] != ' ':
                    num += inp[j][i]
            if len(num):
                nums.append(int(num))

        print(op, nums)
        if op == '+':
            ans += sum(nums)
        else:
            ans += product(nums)


        n += row_w
    print(ans)

main()
