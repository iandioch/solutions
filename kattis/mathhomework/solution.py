*legs, tot = map(int, input().split())

found = False
for i in range(tot//legs[0] + 1):
    for j in range(tot//legs[1] + 1):
        for k in range(tot//legs[2] + 1):
            if legs[0]*i + legs[1]*j + legs[2]*k == tot:
                found |= True
                print(i, j, k)

if not found:
    print('impossible')

