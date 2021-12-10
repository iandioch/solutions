import sys

def get_pair(c):
    pair = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    return pair[c]

# Returns error score
def parse(line):
    OPENS = set('([{<')
    stack = []
    for c in line:
        if c in OPENS:
            stack.append(c)
            continue

        if not len(stack):
            # Expecting an opener, found a closer instead
            print('Line expected to be finished, but found a closer.')
            return 0

        if stack[-1] == get_pair(c):
            stack.pop()
        else:
            print(f'In line "{line}", needed {get_pair(c)} but found {c}')
            return 0

    if len(stack):
        # Line is unfinished
        tot = 0
        score = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }
        for c in stack[::-1]:
            tot *= 5
            tot += score[c]
        return tot
    return 0

def main():
    tot = 0

    scores = []
    for line in sys.stdin.readlines():
        score = parse(line.strip())
        if score > 0:
            scores.append(score)

    scores.sort()
    print(scores[len(scores)//2])

main()
