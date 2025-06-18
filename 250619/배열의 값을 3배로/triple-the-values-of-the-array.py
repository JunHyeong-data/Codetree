matrix = []
for _ in range(3): # 3줄 입력 받기
    row = list(map(int, input().split()))
    matrix.append(row)

# 배열의 모든 원소를 3배로 만듦
for r in range(3):
    for c in range(3):
        matrix[r][c] *= 3

# 변환된 배열 출력
for r in range(3):
    print(" ".join(map(str, matrix[r])))