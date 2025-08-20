# N과 M을 입력받기
n, m = map(int, input().split())

# N x N 크기의 2차원 리스트를 0으로 초기화
arr = [[0] * n for _ in range(n)]

# M개의 점 위치를 입력받아 값 할당
for _ in range(m):
    r, c = map(int, input().split())
    # 1부터 시작하는 행/열 번호를 인덱스로 변환하여 값 할당
    arr[r-1][c-1] = r * c

# 격자 출력
for row in arr:
    print(*row)