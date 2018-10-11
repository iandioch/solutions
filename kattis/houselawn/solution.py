def main():
    min_per_week = 7*24*60
    lawnsize, nummowers = map(int, input().split())
    poss = []
    for i in range(nummowers):
        name, *vals = input().split(',')
        price, speed, battery, recharge_time = map(int, vals)
        tot_cut = min_per_week*speed*battery//(battery + recharge_time)
        if tot_cut >= lawnsize:
            poss.append((price, i, name))
    if len(poss) == 0:
        print('no such mower')
    else:
        poss.sort()
        a = poss[0][0]
        for i in range(len(poss)):
            if poss[i][0] != a:
                break
            print(poss[i][-1])
            


if __name__ == '__main__':
    main()
