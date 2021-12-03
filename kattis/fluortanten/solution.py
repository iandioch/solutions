def main():
    n = int(input())
    vals = list(x for x in map(int, input().split()) if x != 0)

    # This is how it would be were Bjorn at the end of the line.
    curr = sum(vals[i]*(i+1) for i in range(len(vals)))
    best = curr

    # Shift Bjorn forwards in line one space at a time and see
    # what the score would be then.
    for i in range(len(vals)-1, -1, -1):
        curr -= vals[i]*(i+1)
        curr += vals[i]*(i+2)
        if curr > best:
            best = curr

    print(best)

main()
