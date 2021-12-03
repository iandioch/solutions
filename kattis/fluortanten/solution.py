def calc_pos(vals, pos):
    tot = sum(vals[i]*(i+1) for i in range(pos)) + \
          sum(vals[i]*(i+2) for i in range(pos, len(vals)))
    return tot

def main():
    n = int(input())
    vals = list(x for x in map(int, input().split()) if x != 0)
    best = max(calc_pos(vals, i) for i in range(len(vals) + 1))
    print(best)

main()
