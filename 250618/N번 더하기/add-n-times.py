# 정수 A, N을 공백으로 구분하여 입력받습니다.
A, N = map(int, input().split())

# N번 반복하며 A에 N을 더하는 과정을 수행하고 결과를 출력합니다.
for _ in range(N):
    A += N  # A에 N을 더합니다.
    print(A) # 현재 A의 값을 출력합니다.