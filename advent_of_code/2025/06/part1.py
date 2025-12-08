import sys

def product(nums):
    ans = nums[0]
    for n in range(1, len(nums)):
        ans *= nums[n]
    return ans

def main():
    g = []
    for line in sys.stdin.readlines():
        p = line.strip().split(' ')
        print(p)
        n = 0
        for q in p:
            if q == '':
                continue
            if n >= len(g):
                g.append([])
            g[n].append(q)
            n += 1

    print(g)
    ans = 0
    for col in g:
        op = col.pop(-1)
        nums = list(map(int, col))
        if op == '+':
            ans += sum(nums)
        else:
            ans += product(nums)
    print(ans)

main()
