nums = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'onehundred',
    200: 'twohundred',
    300: 'threehundred',
    400: 'fourhundred',
    500: 'fivehundred',
    600: 'sixhundred',
    700: 'sevenhundred',
    800: 'eighthundred',
    900: 'ninehundred'
}

def num_to_str(n):
    if n <= 0:
        return ''
    for i in range(n, 0, -1):
        if i in nums:
            return nums[i] + num_to_str(n-i)

ns = [None] + [num_to_str(i) for i in range(1, 1000)]

m = int(input())
parts = [input().strip() for _ in range(m)]

tot = sum(len(s) for s in parts) - 1

for i in range(1, 1000):
    if tot + len(ns[i]) == i:
        s = [ns[i] if p == '$' else p for p in parts]
        print(' '.join(s))
        break
