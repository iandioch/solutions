def main():
    num_comp, num_query = map(int, input().split())
    company_loc = [-1 for _ in range(num_comp+1)]
    for i, c in enumerate(input().split()):
        company_loc[i+1] = int(c)
    for _ in range(num_query):
        a, b, c = map(int, input().split())
        if a == 1:
            company_loc[b] = c
        else:
            print(abs(company_loc[b] - company_loc[c]))

main()
