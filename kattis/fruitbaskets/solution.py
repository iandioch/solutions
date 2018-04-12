def find_invalid_combos(weights, curr_included, curr, tot):
    if curr == len(weights) or curr_included == 4:
        if tot < 200:
            return tot
        return 0
    ans = find_invalid_combos(weights, curr_included+1, curr+1, tot+weights[curr])
    ans += find_invalid_combos(weights, curr_included, curr+1, tot)
    return ans

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    invalid_tot = find_invalid_combos(weights, 0, 0, 0)
    ans = sum(weights)*(2**(n-1))
    ans -= invalid_tot
    print(ans)

if __name__ == '__main__':
    main()
