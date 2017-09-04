import sys

validhex = set('0123456789abcdef')

for orig in sys.stdin.readlines():
    line = orig.lower()
    i = 0
    while i < len(line) - 1:
        if line[i] == '0' and line[i+1] == 'x':
            num = ''
            for j in range(i+2, len(line)):
                if line[j] not in validhex:
                    break
                num += orig[j]
            if len(num) > 0:
                dec = int(num, base=16)
                print('{}{}{} {}'.format(orig[i],
                                         orig[i+1],
                                         num,
                                         dec))
        i += 1
