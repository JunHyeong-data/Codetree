n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

while True:
    max = -1
    loc = -1

    for i in range(n):
        if a[i] > max:
            max = a[i]
            loc = i
    print(loc+1, end=' ')

    if loc == 0:
        break
    n = loc