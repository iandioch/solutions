def main():
    n = int(input())
    s = map(int, input().split())
    d = {}
    minn = n
    for i, lang in enumerate(s):
        if lang in d:
            minn = min(minn, i - d[lang])
        d[lang] = i
    print(minn)

main()
