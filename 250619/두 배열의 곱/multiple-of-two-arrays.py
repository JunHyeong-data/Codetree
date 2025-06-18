matrix1 = []
for _ in range(3): # 첫 번째 3x3 배열 입력 받기
    row = list(map(int, input().split()))
    matrix1.append(row)

# 두 배열 사이에 있는 '줄 간격' (빈 줄)을 처리
# 이 부분이 IndexError의 원인일 가능성이 매우 높습니다.
input() 

matrix2 = []
for _ in range(3): # 두 번째 3x3 배열 입력 받기
    row = list(map(int, input().split()))
    matrix2.append(row)

result_matrix = []
for r in range(3):
    result_row = []
    for c in range(3):
        # 같은 위치에 있는 수의 곱 계산
        result_row.append(matrix1[r][c] * matrix2[r][c])
    result_matrix.append(result_row)

# 결과 배열 출력
for r in range(3):
    print(" ".join(map(str, result_matrix[r])))