n = int(input())
arr = list(map(int, input().split()))

min_value = max(arr) - min(arr)

for i in range(n):
    for j in range(i+1, n):
        if arr[j] - arr[i] <= min_value:
            min_value = arr[j] - arr[i]
print(min_value)
