n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

min_price = price[0]
max_profit = 0

for i in range(1, n):
    if price[i] - min_price > max_profit:
        max_profit = price[i] - min_price
    if price[i] < min_price:
        min_price = price[i]

print(max_profit)
        
