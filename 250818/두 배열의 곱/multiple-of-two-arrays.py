arr1 = []
while len(arr1) < 3:
    line = input().strip()
    if line:  # 빈 줄 아니면 추가
        arr1.append(list(map(int, line.split())))

arr2 = []
while len(arr2) < 3:
    line = input().strip()
    if line:
        arr2.append(list(map(int, line.split())))

arr3 = [[arr1[i][j] * arr2[i][j] for j in range(3)] for i in range(3)]

for row in arr3:
    print(*row)
