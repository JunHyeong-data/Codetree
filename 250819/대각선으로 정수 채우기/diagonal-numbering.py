N, M = map(int, input().split()) # N과 M을 입력받음
matrix = [[0] * M for _ in range(N)] # 0으로 채워진 N x M 행렬 생성
num = 1 # 채울 숫자 초기화

# 대각선 합 i+j의 값인 k를 기준으로 반복
for k in range(N + M - 1):
    start_i = max(0, k - M + 1)
    end_i = min(k + 1, N)
    for i in range(start_i, end_i):
        j = k - i
        matrix[i][j] = num
        num += 1

# 결과 출력
for row in matrix:
    print(*row)