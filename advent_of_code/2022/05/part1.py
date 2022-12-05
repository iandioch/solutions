import sys

def move1(stacks, a, b):
    stacks[b].append(stacks[a].pop())

def pprint(stacks):
    for i in range(len(stacks)):
        print(i+1, ' '.join(stacks[i]))

def main():
    populating_stacks = True
    stacks = []
    for line in sys.stdin.readlines():
        line = line.rstrip()
        if not line:
            continue

        if ']' not in line:
            if populating_stacks:
                populating_stacks = False
                for s in stacks:
                    s.reverse()
                    # s[0] will now be the bottom of the stack, instead of the top
                print('Finished parsing initial state')
                pprint(stacks)
                continue

        if populating_stacks:
            for i in range(len(line)):
                if line[i] not in '[] ':
                    c = line[i]
                    stackno = (i)//4 # 0-indexed
                    print('putting', c, 'on stack', stackno+1)
                    while len(stacks) <= stackno:
                        stacks.append([])
                    stacks[stackno].append(c)
            continue

        print('-'*10)
        pprint(stacks)
        print('handling', line)
        # move N from A to B
        p = line.split()
        n = int(p[1])
        a = int(p[3])-1
        b = int(p[5])-1
        for _ in range(n):
            move1(stacks, a, b)
        print('after:')
        pprint(stacks)

    print(''.join(s.pop() for s in stacks))




main()
