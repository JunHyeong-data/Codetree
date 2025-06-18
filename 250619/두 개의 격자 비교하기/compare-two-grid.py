N, M = map(int, input().split())

matrix1 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix1.append(row)

# 첫 번째 격자 입력 후 빈 줄이 없으므로, 추가 input() 없이 바로 두 번째 격자 입력
# 이미지의 입력 설명을 다시 보면 "N+2번째 줄부터"라고 되어 있으므로,
# 첫 번째 격자 입력 후 추가적인 input() 호출 없이 바로 다음 N줄이 두 번째 격자입니다.
# 만약 IndexError가 발생한다면, N+1번째 줄에 빈 줄이 있을 가능성이 있습니다.
# 이전 문제와 유사하게 "줄 간격을 사이에 두고 주어집니다" 문구가
# 이번에도 빈 줄을 의미하는지 확인이 필요합니다.
# 일단 "N+2번째 줄부터"라는 명시적인 설명에 따라 빈 줄 처리 없이 진행합니다.

matrix2 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix2.append(row)


result_matrix = []
for r in range(N):
    result_row = []
    for c in range(M):
        if matrix1[r][c] == matrix2[r][c]:
            result_row.append(0)
        else:
            result_row.append(1)
    result_matrix.append(result_row)

for r in range(N):
    print(" ".join(map(str, result_matrix[r])))