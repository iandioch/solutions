import operator
from functools import lru_cache, reduce

@lru_cache(maxsize=None)
def go(s):
    return reduce(operator.mul, (int(c) for c in s if c != '0'))

def main():
    s = input()
    while len(s) > 1:
        s = str(go(s))
    print(s)

main()
