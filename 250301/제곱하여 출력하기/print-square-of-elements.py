n = int(input())
result = list(map(int, input().split()))

newResult = [elem ** 2 for elem in result]
for i in newResult:
    print(i, end=' ')