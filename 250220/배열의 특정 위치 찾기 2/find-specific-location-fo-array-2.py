arr = list(map(int, input().split()))

result1 = arr[0:9:2]
result2 = arr[1:9:2]

if sum(result1) > sum(result2):
    print(sum(result1) - sum(result2))
else:
    print(sum(result2) - sum(result1))