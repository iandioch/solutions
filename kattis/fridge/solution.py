s = input()
d = {i:s.count(str(i)) for i in range(10)}
digs = sorted(sorted(d.keys()), key=lambda x: d[x])

done = False
for i in range(1, 10):
    if d[i] == 0:
        print(i)
        done = True
        break

if not done:
    least_common_num = digs[0]
    if least_common_num == 0:
        #edge case
        if d[0]  < d[digs[1]]:
            print('1' + '0'*(d[0]+1))
            done = True
        else:
            least_common_num = digs[1]
    if not done:
        print(str(least_common_num)*(d[least_common_num]+1))
    
