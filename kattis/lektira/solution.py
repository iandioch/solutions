def main():
    s = input().strip()
    ans = 'zzzzzzzzzzzzzz'
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            a = s[:i][::-1] 
            b = s[i:j][::-1]
            c = s[j:][::-1]
            t = a + b + c
            ans = min(t, ans)
    print(ans)

main()
