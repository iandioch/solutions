def calc(a, b, k):
    ans = b-a
    if ans <= 1:
        return ans
    naa = k # Nearest multiple of k above a
    nbb = (b//k)*k # Nearest multiple of k below b
    if nbb == 0:
        nbb += k
    ans = min(ans, 1 + (naa-a) + (b-nbb))
    return ans

b, k = map(int, input().split())
print(calc(0, b-1, k))
