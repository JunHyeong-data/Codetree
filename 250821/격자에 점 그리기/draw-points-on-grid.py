n, m = list(map(int, input().split()))
loc = [input() for _ in range(m)]

arr = [[0]*n for _ in range(n)]
cnt = 1
for elem in loc:
    a, b = map(int, elem.split())
    arr[a-1][b-1] = cnt
    cnt += 1

for elem in arr:
    print(*elem)

