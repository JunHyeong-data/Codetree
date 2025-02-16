n = int(input())

for i in range(n):
    prod = 1
    a, b = map(int, input().split())
    for j in range(a, b+1):#a부터 b까지의 곱
        prod *= j
    print(prod)