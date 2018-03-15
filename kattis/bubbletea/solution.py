n = int(input())
tea_prices = list(map(int, input().split()))
input()
topping_prices = list(map(int, input().split()))
min_price = None
for i in range(n):
    k, *p = list(map(int, input().split()))
    for q in p:
        price = tea_prices[i] + topping_prices[q-1]
        if not min_price or min_price > price:
            min_price = price
num = int(input())//min_price
print(max(num-1, 0))
