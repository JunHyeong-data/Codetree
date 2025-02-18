arr = list(map(int, input().split()))
cnt = 0
result = []
for elem in arr:
    if elem == 0:
        break
    else:
        result.append(elem)
print((arr[len(result)-1]+arr[len(result)-2]+arr[len(result)-3]))