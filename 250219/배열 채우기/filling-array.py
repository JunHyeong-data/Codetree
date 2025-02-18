arr = list(map(int, input().split()))

result = []
for elem in arr:
    if elem == 0:
        break
    else:
        result.append(elem)
for num in result[::-1]:
    print(num, end=' ')