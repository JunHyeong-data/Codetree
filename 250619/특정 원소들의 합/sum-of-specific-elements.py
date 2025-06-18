matrix = []
for _ in range(4): # 4줄의 입력을 받아서 2차원 배열 생성
    row = list(map(int, input().split()))
    matrix.append(row)

total_sum = 0

# 예시 설명에 해당하는 칸들의 값을 더함 (0-indexed)
total_sum += matrix[0][0] # 3
total_sum += matrix[1][0] # 2
total_sum += matrix[1][1] # 6
total_sum += matrix[2][0] # 3
total_sum += matrix[2][1] # 31
total_sum += matrix[2][2] # 2
# total_sum += matrix[2][3] # 1 (예시 설명에는 이 값이 없습니다. 그림에는 있지만)

total_sum += matrix[3][0] # 95
total_sum += matrix[3][1] # 5
total_sum += matrix[3][2] # 7
total_sum += matrix[3][3] # 1

print(total_sum)