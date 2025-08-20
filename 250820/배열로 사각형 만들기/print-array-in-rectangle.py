arr = [[0]*5 for _ in range(5)]

# 첫번째 행과 첫 번째 열에 전부 숫자 1을 채운다
for i in range(5):
    for j in range(5):
        if i == 0:
            arr[i][j] = 1
        elif j == 0:
            arr[i][j] = 1
# 나머지 칸들 바로 위의 값과 바로 왼쪽의 값을 더하니다.
for i in range(1, 5):
    for j in range(1, 5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for elem in arr:
    print(*elem)