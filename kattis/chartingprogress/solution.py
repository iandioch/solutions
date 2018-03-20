import sys

vals = []
m = 0

def output_graph():
    global vals

    n = 0
    for v in vals:
        s = '.'*(m - v - n) + '*'*v + '.'*n
        n += v
        print(s)

    vals = []

for line in sys.stdin.readlines():
    if len(line.strip()) == 0:
        output_graph()
        print()
    else:
        t = 0
        for c in line:
            if c == '*':
                t += 1
        m = len(line.strip())
        vals.append(t)


output_graph()
