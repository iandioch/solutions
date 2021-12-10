import sys

def get_score(c):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return scores[c]

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
            return get_score(c)

        if stack[-1] == get_pair(c):
            stack.pop()
        else:
            print(f'In line "{line}", needed {get_pair(c)} but found {c}')
            return get_score(c)

    if len(stack):
        # Line is unfinished
        return 0
    return 0

def main():
    tot = 0
    for line in sys.stdin.readlines():
        tot += parse(line.strip())
    print(tot)

main()
