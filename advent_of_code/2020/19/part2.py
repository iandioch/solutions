import sys
import functools
from enum import Enum

class Token(Enum):
    LITERAL = 1
    RULE = 2

def main():
    def parse_rule(s):
        rule = []
        for opt in s.split('|'):
            subrule = []
            for part in opt.split():
                if part[0] == '"':
                    subrule.append((Token.LITERAL, part.split('"')[1]))
                else:
                    subrule.append((Token.RULE, int(part)))
            rule.append(subrule)
        return rule

    rules = {}

    @functools.lru_cache(maxsize=None)
    def get_sentences_for_rule(num):
        ret = []
        for opt in rules[num]:
            vals = [''] 
            for part_type, val in opt:
                if part_type is Token.LITERAL:
                    for i in range(len(vals)):
                        vals[i] += val
                else:
                    newvals = []
                    for rest in get_sentences_for_rule(val):
                        for i in range(len(vals)):
                            newvals.append(vals[i] + rest)
                    vals = newvals
            ret += vals
        if any(len(r) > 97 for r in ret):
            return []
        return ret

    poss42 = set() # All possible sentences formed from rule 42
    poss31 = set() # All possible sentences formed from rule 31

    # Return the number of rule 31 invocs to create the string s, or -1 if not poss
    def num_31s(s):
        if len(s) == 0:
            return 0
        for t in poss31:
            if s.startswith(t):
                rest = num_31s(s[len(t):])
                if rest >= 0:
                    return 1 + rest
        return -1

    def num_42s(s):
        # Return generator yielding (# rule 42s, # rule 31s) to make string s
        if len(s) == 0:
            return -1, - 1
        for t in poss42:
            if s.startswith(t):
                rest = num_42s(s[len(t):])
                for a, b in rest:
                    if a < 0 or b < 0:
                        continue
                    yield a+1, b
                rest = num_31s(s[len(t):])
                if rest >= 0:
                    yield 1, rest
        return -1, -1

    def is_poss(s):
        for a, b in num_42s(s):
            if a >= 2 and b >= 1 and a > b:
                return True
        return False


    done_rules = False
    ans = 0
    for line in sys.stdin.readlines():
        if line.strip() == '':
            done_rules = True
            poss42 = set(get_sentences_for_rule(42))
            poss31 = set(get_sentences_for_rule(31))
            continue
        if done_rules:
            if is_poss(line.strip()):
                ans += 1
        else:
            rule_no, rule = line.split(':')
            rules[int(rule_no)] = parse_rule(rule)
    print(ans)

main()
