import sys

lines = sys.stdin.readlines()
curr_line = 0
while curr_line < len(lines):
    n = int(lines[curr_line])
    stack = []
    stackposs = True
    queue = []
    queueposs = True
    prio = []
    prioposs = True
    for _ in range(n):
        curr_line += 1
        op, val = map(int, lines[curr_line].split())
        if op == 1:
            stack.append(val)
            queue.append(val)
            prio.append(val)
        else:
            if stackposs:
                if len(stack):
                    if stack[-1] != val:
                        stackposs = False
                    else:
                        del stack[-1]
                else:
                    stackposs = False
            if queueposs:
                if len(queue):
                    if queue[0] != val:
                        queueposs = False
                    else:
                        del queue[0]
                else:
                    queueposs = False
            if prioposs:
                if len(prio):
                    index = 0
                    maxval = prio[0]
                    for i in range(1, len(prio)):
                        if prio[i] > maxval:
                            maxval = prio[i]
                            index = i
                    if maxval != val:
                        prioposs = False
                    else:
                        del prio[index]
                else:
                    prioposs = False
    poss = 0
    if stackposs:
        poss += 1
    if queueposs:
        poss += 1
    if prioposs:
        poss += 1
    if poss == 0:
        print('impossible')
    elif poss > 1:
        print('not sure')
    else:
        if stackposs:
            print('stack')
        elif queueposs:
            print('queue')
        else:
            print('priority queue')
    curr_line += 1
    

