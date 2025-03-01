arr = list(map(int, input().split()))

for i in range(10):
    if arr[i]+arr[i+1] >= 10:
        arr[i+1] %= 10
    arr.append(arr[i]+arr[i+1])

for i in range(10):
    print(arr[i], end=' ')


