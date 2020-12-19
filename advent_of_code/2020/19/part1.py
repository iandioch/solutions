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
        print('get_sentences_for_rule({})'.format(num))
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
        return ret

    poss_sentences = set()
    done_rules = False
    ans = 0
    for line in sys.stdin.readlines():
        if line.strip() == '':
            print(rules)
            done_rules = True
            poss_sentences = set(get_sentences_for_rule(0))
            continue
        if done_rules:
            if line.strip() in poss_sentences:
                ans += 1
        else:
            rule_no, rule = line.split(':')
            rules[int(rule_no)] = parse_rule(rule)
    print(ans)

main()
