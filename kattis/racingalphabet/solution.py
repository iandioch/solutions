import math
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

def get_arc(num_letters):
    num_letters %= 28
    return 2*math.pi*30*(num_letters/28)

def get_len(curr, other):
    a = A.find(curr)
    b = A.find(other)
    return min(get_arc(b-a), get_arc(a-b))

n = int(input())
for _ in range(n):
    s = input()
    c = s[0]
    a = 0
    for d in s[1:]:
        a += get_len(c, d)/15
        c = d
    print(a + len(s))
