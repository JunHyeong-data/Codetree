n = int(input())

cnt = 0
num = 1
arr = [[0]*n for _ in range(n)]

for j in range(n-1,-1,-1):
    if cnt % 2 == 0:
        for i in range(n-1,-1,-1):
            arr[i][j] = num
            num += 1
    else:
        for i in range(n):
            arr[i][j] = num
            num += 1
    cnt +=1
for elem in arr:
    print(*elem)
