n = int(input())

arr = list(map(int, input().split()))
result = []
for elem in arr[::-1]:
    if elem % 2 == 0:
        result.append(elem)

for j in range(len(result)):
    print(result[j], end=' ')
