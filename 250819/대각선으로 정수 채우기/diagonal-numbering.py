n, m = map(int, input().split())

# Please write your code here.

numlist = [[0] * m for _ in range(n)]

cnt = 0

for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                cnt += 1
                numlist[i][j] = cnt
                

for row in numlist:
    for elem in row:
        print(elem, end=" ")
    print()

